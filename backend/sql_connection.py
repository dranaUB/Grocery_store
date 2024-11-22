import datetime
import psycopg2
from psycopg2 import pool

import os

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING

__cnx = None

def get_sql_connection():
  # print("Opening postgressql connection")
    global __cnx
    conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
    conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

    if __cnx is None:
      __cnx = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
      dbuser=conn_str_params['user'],
      dbpass=conn_str_params['password'],
      dbhost=conn_str_params['host'],
      dbname=conn_str_params['dbname']
      )

    return __cnx
