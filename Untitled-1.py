import sqlite3
from sqlite3 import Error

def create_connection(db_file):



   conn = sqlite3.connect(db_file)
   return conn

def execute_sql(conn, sql):
   
   c = conn.cursor() 
   c.execute(sql)
   results = c
   return results

def add_project(conn, project):
   sql = '''INSERT INTO project(nazwa, start_date, end_date)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, project)
   return cur.lastrowid

def add_task(conn, task):
   sql = '''INSERT INTO tasks(projekt_id, nazwa, opis, status, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, task)
   conn.commit()
   return cur.lastrowid

def select_project(conn ,task_1):
   
   cur = conn.cursor()
   cur.execute(task_1)
   f = cur.fetchone()
   
   return  f 
def select_tasks(conn ,task_2):
   
   cur = conn.cursor()
   cur.execute(task_2)
   h = cur.fetchmany(1)
   return  h    

def update(conn , table, parameter , nazwa ,value):
   sql = f''' UPDATE {table} SET {parameter}=? WHERE id=?'''
   cur = conn.cursor()
   cur.execute(sql ,(nazwa ,value))   
   conn.commit()
      

def delete_where(conn,  id):
   sql = 'DELETE FROM tasks WHERE id=?'
   cur = conn.cursor()
   cur.execute(sql ,(id,))
   conn.commit()


   

if __name__ == '__main__':

     
   create_projects_sql = """
   -- project table
   CREATE TABLE IF NOT EXISTS project (
      id integer PRIMARY KEY,
      nazwa text NOT NULL,
      start_date text,
      end_date text
   );
   """

   create_tasks_sql =  """
   -- zadanie table
   CREATE TABLE IF NOT EXISTS tasks (
      id integer PRIMARY KEY,
      projekt_id integer NOT NULL,
      nazwa VARCHAR(250) NOT NULL,
      opis TEXT,
      status VARCHAR(15) NOT NULL,
      start_date text NOT NULL,
      end_date text NOT NULL,
      FOREIGN KEY (projekt_id) REFERENCES projects (id)
   );"""
   
   conn = create_connection("database.db")
   
   execute_sql(conn, create_projects_sql)
   execute_sql(conn, create_tasks_sql)
   
   project = ("Powtórka z angielskiego", "2020-05-11 00:00:00", "2020-05-13 00:00:00")
   pr_id= add_project(conn, project) 
   task = (pr_id,"Czasowniki regularne","Zapamiętaj czasowniki ze strony 30","started","2020-05-11 12:00:00","2020-05-11 15:00:00")
   task_id = add_task(conn , task)
   task_1 ="""SELECT * FROM project ;"""
   task_2 ="""SELECT * FROM tasks ;"""
   print(select_project(conn , task_1))
   print(select_tasks(conn ,task_2))
   update( conn,table="project", parameter="nazwa" ,nazwa="Powtórka z niemieckiego" ,value=1)
   id=2
   delete_where(conn ,id)
   