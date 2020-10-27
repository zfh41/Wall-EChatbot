# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import flask
import flask_sqlalchemy
import flask_socketio
# import models 
# import psycopg2
import requests
import json
from datetime import datetime
from flask_socketio import join_room, leave_room
import random
import urllib.parse as parse
from rfc3987 import parse



ADDRESSES_RECEIVED_CHANNEL = 'addresses received'

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

SQL_USER='SQL_USER'
SQL_PASSWORD='SQL_PASSWORD'
SQL_USER='SQL_USER'

global loginUser
loginUser=''
global num_users
global new_user
global imageURL
global userLength
global address
global dbuser

sql_user = os.environ[SQL_USER]
sql_pwd = os.environ[SQL_PASSWORD]
dbuser = os.environ[SQL_USER]



address=''
userLength=0
imageURL=''
num_users = 0
global isUrl
isUrl=1

database_uri = os.environ['DATABASE_URL']


app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)

import models 
import psycopg2



db.init_app(app)
db.app = app


db.create_all()
db.session.commit() 


def emit_all_addresses(channel):
    all_addresses=[db_address.address for db_address in db.session.query(models.Usps).all()]
    checkUrl=[db_urls.url for db_urls in db.session.query(models.Usps).all()]
    dbusers=[db_users.guser for db_users in db.session.query(models.Usps).all()]
    imgUrls=[db_imgurls.imgurl for db_imgurls in db.session.query(models.Usps).all()]
    print("num_users: " + str(num_users))
    
    print("lol" + imageURL)
    
    socketio.emit(channel, {
        'allAddresses':all_addresses, 'User':dbusers, 'numUsers': num_users, 'imageURL':imgUrls, 'address':address, 'isUrl':isUrl,'checkUrl':checkUrl
    })
    

def push_new_user_to_db(name, auth_type):
    # TODO remove this check after the logic works correctly
    if name != "John Doe":
        db.session.add(models.AuthUser(name, auth_type));
        db.session.commit();
        

@socketio.on('connect')
def on_connect():
    
    global num_users
    
    num_users+=1
    
    print('Someone connected!')
    
    socketio.emit('connected', {
        'test':'Connected'
    })
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)
    

@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')
    global num_users
    num_users-=1
    socketio.emit('disconnected', {
        'test': 'Disconnected'
    })
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)
    
@socketio.on('new google user')
def on_new_google_user(data):
    print("Got an event for new google user input with data:", data['name'])
    push_new_user_to_db(data['name'], models.AuthUserType.GOOGLE);
    global loginUser
    global imageURL
    loginUser=data['name']
    print("loginuser: " + loginUser)
    imageURL=data['imageURL']
    print("lol" + imageURL)
    socketio.emit('connected', {
        'test':'Connected'
    })
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)
    
    return data['name']
    
    

@socketio.on('new address input')
def on_new_address(data):
    print("Got an event for new address input with data:", data)
    global dbuser
    global isUrl
    dbuser = loginUser
    print(dbuser)
    global address;
    address=data["address"]
    message=address
    
    
    try:
        parse(data["address"], rule='IRI')
        isUrl=address
        # if (isUrl[-4:] ==".png" or isUrl[-4:]==".jpg" or isUrl[-4:]==".gif"):
            
    except:
        print("whoa")
        isUrl="1"
    
        
    
    print("isUrl: " + isUrl);
    db.session.add(models.Usps(message, isUrl, dbuser, imageURL));
    db.session.commit();
    
    # room = data['room']
    # join_room(room)
    
    if(data["address"][0:2] == '!!'):
        dbuser="wall-Ebot"
        if(data["address"][2:] == 'about'):
            message=dbuser+": "+"Hi I am Wall-E, nice to meet you. I am a robot that likes to clean up the Earth!"
        elif(data["address"][2:] == "help"):
            message=dbuser+": "+"Commands that can be used: !!about, !!funtranslate <message>, !!pun, !!time"
        elif(data["address"][2:14] == "funtranslate"):
            url='https://api.funtranslations.com/translate/yoda.json?text={}'.format(data["address"][15:])
            response = requests.get(url)
            json_body = response.json()
            print(json_body)
            message=dbuser+": "+(json.dumps(json_body["contents"]["translated"])).strip('\"\\n')
        elif(data["address"][2:] == "pun"):
           url='https://sv443.net/jokeapi/v2/joke/Pun?type=single'
           response = requests.get(url)
           json_body = response.json()
           message=dbuser+": "+(json.dumps(json_body["joke"])).strip('\"\\n')
           print(json.dumps(json_body["joke"]))
        elif(data["address"][2:] == "time"):
            message=dbuser+": The time is "+str(datetime.now().time().strftime("%I:%M %p"))
        else:
            message=dbuser+": "+"Sorry I do not recognize this command..."
        
        
        db.session.add(models.Usps(message, isUrl, dbuser, imageURL));
        db.session.commit();
    
    emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)
    return message

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