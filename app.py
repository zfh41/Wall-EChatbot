# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import flask
import flask_sqlalchemy
import flask_socketio
import models 
import psycopg2

ADDRESSES_RECEIVED_CHANNEL = 'addresses received'

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

sql_user = os.environ['SQL_USER']
sql_pwd = os.environ['SQL_PASSWORD']
dbuser = os.environ['SQL_USER']

database_uri = 'postgresql://{}:{}@localhost/postgres'.format(
    sql_user, sql_pwd)

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app


db.create_all()
db.session.commit()

users=[]
def emit_all_addresses(channel, dbuser):
    all_addresses=[db_address.address for db_address in db.session.query(models.Usps).all()]
    
    socketio.emit(channel, {
        'allAddresses':all_addresses, 'User':dbuser
    })

@socketio.on('connect')
def on_connect():
    print('Someone connected!')
    socketio.emit('connected', {
        'test': 'Connected'
    })
    
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL, dbuser)
    

@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')

@socketio.on('new address input')
def on_new_address(data):
    print("Got an event for new address input with data:", data)
    
    db.session.add(models.Usps(data["address"]));
    print(data["address"])
    db.session.commit();
    
    if(data["address"][0:2] == '!!'):
        dbuser="wall-Ebot"
        db.session.add(models.Usps("bot has arrived."))
        db.session.commit();
    else:
        dbuser= os.environ['SQL_USER']
    
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL, dbuser)

@app.route('/')
def index():
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL, dbuser)

    return flask.render_template("index.html")

if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )