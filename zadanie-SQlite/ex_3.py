# ex_03.py
import sqlite3

def create_connection(db_file):
   """ create a database connection to the SQLite database2
       specified by db_file
   :param db_file: database2 file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn

def add_lekciia(conn, lekciia):
   """
   Create a new lekciia into the lekciia table
   :param conn:
   :param lekciia:
   :return: lekciia id
   """
   sql = '''INSERT INTO lekciia(name, start_date, end_date)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, lekciia)
   conn.commit()
   return cur.lastrowid

def add_zadanie(conn, zadanie):
   """
   Create a new zadanie into the zadanie table
   :param conn:
   :param zadanie:
   :return: zadanie id
   """
   sql = '''INSERT INTO zadanie(lekciia_id, name, description, status, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, zadanie)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":
  lekciia = ("Повторення англійської", "2023-03-04 00:00:00", "2023-03-05 00:00:00")

  conn = create_connection("database2.db")
  pr_id = add_lekciia(conn, lekciia)

  zadanie = (
       pr_id,
       "Правильні дієслова",
       "Запам’ятай дієслова на сторінці 30",
       "started",
       "2020-05-11 12:00:00",
       "2020-05-11 15:00:00"
   )
  zadanie = (
       pr_id,
       "Не правильні дієслова",
       "Запам’ятай дієслова на сторінці 56",
       "started",
       "2020-05-11 12:00:00",
       "2020-05-11 15:00:00"
   )

  zadanie_id = add_zadanie(conn, zadanie)

  print(pr_id, zadanie_id)
  conn.commit()