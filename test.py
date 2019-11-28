#! /usr/bin/env python3
from flask import Flask,render_template
from flask_socketio import SocketIO
import time


#from Car import *
app = Flask(__name__)
app.config['SECRET_iEY'] ='secret'
socketio=SocketIO(app)

@app.route('/')
def index():
    return render_template('Car_test.html')

@socketio.on('action')
def hanlde_message(msg):
    action=msg['action']
    if action=='forward':
        #car.forward()
        print(action)
 

@socketio.on('connect')
def test_connect():
    print("socketio connect successful!")



if __name__=='__main__':
    print("listening localhost:5000")
    t= threading.Thread(target=avoidance)
    t.setDaemon(True)#设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
    socketio.run(app, debug=False,host='0.0.0.0')
#！/usr/bin/env python 3
从烧瓶导入瓶，呈现_模板
从烧瓶_Socketio进口SocketIO
import time


#from Car import *
app = Flask(__name__)
app.config['SECRET_iEY'] ='secret'
Socketio=SocketIO(APP)

@app.path(‘/’)
def index():
    return render_template('Car_test.html')

@socketio.on(“行动”)
def hanlde_message(msg):
action=msg[‘action’]
如果行动=‘前进’：
        #car.forward()
印刷(行动)
 

@socketio.on('connect')
def test_connect():
    print("socketio connect successful!")



如果_name__==‘_main_’：
    print("listening localhost:5000")
线程(目标=避免)
    t.setDaemon(True)#设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
    socketio.run(app, debug=False,host='0.0.0.0')
