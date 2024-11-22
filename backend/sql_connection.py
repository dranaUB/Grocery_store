import datetime
import psycopg2
from psycopg2 import pool


__cnx = None

def get_sql_connection():
  print("Opening postgressql connection")
  global __cnx

  if __cnx is None:
    __cnx = psycopg2.connect(database = "FIRST_SAMPLE_DATABASE", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "727272",
                        port = 5432)

  return __cnx