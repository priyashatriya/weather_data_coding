import sqlite3
from flask_swagger_ui import get_swaggerui_blueprint

def get_condition(args, pair):
    conditions = []
    for k,v in pair.items():
        if k in args:
            param = args[k]
            conditions.append(f"{v}='{param}'")
    condition = ""
    if len(conditions):
        condition =" where " + " and ".join(condition)
    return condition

def get_curser():
    #Connect to sqlite data
    conn = sqlite3.connect('../assessment.db')
    # get curser
    return conn.cursor()

def to_json(data, success = True, msg = "successfull"):
    response =  jsonify({
        "success": success,
        "data": data,
        "message": msg
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def all_swagger_docs(app):
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
     SWAGGER_URL,
        API_URL,
        config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    app.register_blueprint(swaggerui_blueprint)