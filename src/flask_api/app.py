from utils import *
from flask import  Flask,request

#Create Flask APP
app = Flask(__name__)



all_swagger_docs(app)

@app.route('/api/weather/', methods = ['GET'])
def get_weather_api():
    args = request.args
    cursor = get_curser()
    condition = get_condition(args, {'date':'record_date', 'station':"region"})
    cursor.execute(f'SELECT * FROM WEATHER_DATA_TABLE {condition};')
    records = cursor.fetchall()
    data = [ list(row) for row in records ]
    return to_json(data)

@app.route('/api/weather/stats/', methods = ['GET'])
def get_weather_stats_api():
    args = request.args
    cursor = get_curser()
    condition = get_condition(args, {'year':'year', 'station':"region"})
    cursor.execute(f'SELECT * FROM ANALYTICS_DATA_TABLE {condition}')
    record = cursor.fetchall()
    data = [ list(row) for row in record ]
    return to_json(data)


if __name__ == '__main__':
    #start application
    app.run(debug = True)


    
    