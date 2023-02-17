import os
import sqlite3

def get_curser():
    #Connect to sqlite data
    conn = sqlite3.connect('../assessment.db')
    # get curser
    return conn.cursor()

def read_all_files(path):
   files_names = []
   for f_name in os.listdir(path):
       if f_name.endswith(".txt"): 
            files_names.append(os.path.join(path, f_name))
   return files_names

def create_table(curser, ddl_path):
    
    # reading  ddl files
    with open(f"ddls/{ddl_path}", "r") as fb:
            sql_query = fb.read()
            curser.execute(sql_query) 
            print(f"Executed ddl query {sql_query}")
            print("Table created successfully........")