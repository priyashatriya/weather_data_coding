from utils import *
from constants import *
from datetime import datetime


#get cursor 
curser = get_curser()

# create model
create_table(curser, ANALYTICS_DDL_FILE)

SQL_QUERY = """
insert into ANALYTICS_DATA_TABLE
select aa.station, aa.Year , avg_min_tem, avg_max_tem, total_acc_participation
from (
select region as station, strftime('%Y',record_date) as "Year" from WEATHER_DATA_TABLE group by region, strftime('%Y',record_date)
) aa
left join (
select region as station, strftime('%Y',record_date) as "Year",  avg(min_temperature) as avg_min_tem, avg(max_temperature) as avg_max_tem, sum(participation) as total_acc_participation
from WEATHER_DATA_TABLE
where min_temperature != -9999 and max_temperature != -9999 and participation != 9999
group by region, strftime('%Y',record_date) ) bb 
on aa.station = bb.station and aa.year = bb.Year ;
"""

curser.execute(SQL_QUERY)

print("Data Analytics Table generated successfully")

