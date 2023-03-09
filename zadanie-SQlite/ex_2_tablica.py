# ex_02_create_tables.py

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database2 file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":

   create_lekciia_sql = """
   -- projects table
   CREATE TABLE IF NOT EXISTS lekciia (
      id integer PRIMARY KEY,
      name text NOT NULL,
      start_date text,
      end_date text
   );
   """

   create_zadanie_sql = """
   -- tasks table
   CREATE TABLE IF NOT EXISTS zadanie (
      id integer PRIMARY KEY,
      lekciia_id integer NOT NULL,
      name VARCHAR(250) NOT NULL,
      description TEXT,
      status VARCHAR(15) NOT NULL,
      start_date text NOT NULL,
      end_date text NOT NULL,
      FOREIGN KEY (lekciia_id) REFERENCES lekciia (id)
   );
   """

   db_file = "E:\Kodilla1\learning-git-13 base\database2.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_lekciia_sql)
       execute_sql(conn, create_zadanie_sql)


conn.close()