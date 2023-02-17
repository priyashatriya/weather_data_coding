from utils import *
from constants import *
from datetime import datetime


def insert_weather_data(curser, records, f_path):
    rows = []
    clean_data = f_path.split("/")[-1].split(".")[0]
    for record in records:
        datas = record.split("\t")
        clean_date = datetime.strptime(datas[0], '%Y%m%d')
        rows.append((clean_data, clean_date, datas[1], datas[2], datas[3]))
    curser.executemany('INSERT  INTO WEATHER_DATA_TABLE VALUES(?,?,?,?,?) ;',rows)

def insert_yield_data(curser, records, f_path):
    rows = []
    clean_data = f_path.split("/")[-1].split(".")[0]
    for record in records:
       datas = record.split("\t")
       rows.append((clean_data, datas[0], datas[1]))
    curser.executemany('INSERT INTO YIELD_TABLE VALUES(?,?,?) ;',rows)

def insert_records(curser, path, func):
    # inserting data to data tables
    files = read_all_files(path)
    for f_path in files:
        with open(f_path, "r") as fb_obj:
            records = fb_obj.readlines()
        func(curser, records, f_path)

#get cursor 
curser = get_curser()

for f_path in INPUT_DDL_FILES:
    # create models 
    create_table(curser, f_path)


#inserting records for weather and yield data
insert_records(curser,WEATHER_PATH, insert_weather_data)
insert_records(curser,YIELD_PATH, insert_yield_data)
            








