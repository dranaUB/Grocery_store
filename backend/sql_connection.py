import os
import psycopg2
from psycopg2 import pool

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING

__cnx = None  # This will store your connection object

def get_sql_connection():
    global __cnx
    if __cnx is None:
        # Retrieve the connection string from the environment variable
        conn_str = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING')
        if not conn_str:
            raise EnvironmentError("AZURE_POSTGRESQL_CONNECTIONSTRING environment variable is not set.")

        # Parse the connection string into parameters
        conn_str_params = {}
        for pair in conn_str.strip().split():
            key, value = pair.split('=', 1)
            conn_str_params[key] = value

        required_params = {'user', 'password', 'host', 'dbname'}
        missing_params = required_params - conn_str_params.keys()
        if missing_params:
            raise ValueError(f"Missing required connection parameters: {', '.join(missing_params)}")

        # Establish the connection using psycopg2
        try:
            __cnx = psycopg2.connect(
                user=conn_str_params['user'],
                password=conn_str_params['password'],
                host=conn_str_params['host'],
                dbname=conn_str_params['dbname']
            )
            print("Database connection established.")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")
            raise

    return __cnx  # Returns the connection object
