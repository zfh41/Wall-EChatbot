# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import flask
import flask_sqlalchemy
import flask_socketio
import models 
import psycopg2
import requests
import json

ADDRESSES_RECEIVED_CHANNEL = 'addresses received'

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

SQL_USER='SQL_USER'
SQL_PASSWORD='SQL_PASSWORD'
SQL_USER='SQL_USER'

sql_user = os.environ[SQL_USER]
sql_pwd = os.environ[SQL_PASSWORD]
dbuser = os.environ[SQL_USER]


database_uri = 'postgresql://{}:{}@localhost/postgres'.format(
    sql_user, sql_pwd)

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app


db.create_all()
db.session.commit()


def emit_all_addresses(channel):
    all_addresses=[db_address.address for db_address in db.session.query(models.Usps).all()]
    
    socketio.emit(channel, {
        'allAddresses':all_addresses
    })

@socketio.on('connect')
def on_connect():
    print('Someone connected!')
    socketio.emit('connected', {
        'test': 'Connected'
    })
    
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)
    

@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')

@socketio.on('new address input')
def on_new_address(data):
    print("Got an event for new address input with data:", data)
    dbuser = os.environ['SQL_USER']
    message=dbuser+": "+data["address"]
    db.session.add(models.Usps(message));
    print(data["address"])
    db.session.commit();
    
    if(data["address"][0:2] == '!!'):
        dbuser="wall-Ebot"
        if(data["address"][2:] == 'about'):
            message=dbuser+": "+"Hi I am Wall-E, nice to meet you. I am a robot that likes to clean up the Earth!"
        elif(data["address"][2:] == "help"):
            message=dbuser+": "+" Commands that can be used: !!about, !!funtranslate <message>, !!pun"
        elif(data["address"][2:14] == "funtranslate"):
            url='https://api.funtranslations.com/translate/yoda.json?text={}'.format(data["address"][15:])
            response = requests.get(url)
            json_body = response.json()
            message=dbuser+": "+(json.dumps(json_body["contents"]["translated"])).strip('\"\\n')
            print(json.dumps(json_body))
        elif(data["address"][2:] == "pun"):
           url='https://sv443.net/jokeapi/v2/joke/Pun?type=single'
           response = requests.get(url)
           json_body = response.json()
           message=dbuser+": "+(json.dumps(json_body["joke"])).strip('\\\n"')
           print(json.dumps(json_body["joke"]))
        else:
            message=dbuser+": "+"Sorry I do not recognize this command..."

        db.session.add(models.Usps(message));
        db.session.commit();
    
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)

@app.route('/')
def index():
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)

    return flask.render_template("index.html")

if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )