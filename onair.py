#!/usr/bin/python3
import psutil
import subprocess
import blinkt
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

loop_py_path = '/usr/local/sbin/onair/loop.py'
def start_onair(effect):
    if effect == 'stop':
        loop_pid = [proc.pid for proc in psutil.process_iter() if loop_py_path in proc.cmdline()]
        for loop in loop_pid:
            command = ['kill','-9',str(loop)]
            subprocess.Popen(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        blinkt.clear()
        blinkt.show()
    else:
        blinkt.clear()
        blinkt.show()
        loop_pid = [proc.pid for proc in psutil.process_iter() if loop_py_path in proc.cmdline()]
        for loop in loop_pid:
            command = ['kill','-9',str(loop)]
            subprocess.Popen(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        command = ['/usr/bin/python3',loop_py_path,'-e',effect]
        subprocess.Popen(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

class OnAir(Resource):
    def get(self, status):
        if status == 'stop':
            start_onair(status)
            start_onair(status)
        elif status == 'breathing':
            start_onair(status)
        elif status == 'breathing_two':
            start_onair(status)
        elif status == 'processing':
            start_onair(status)
        elif status == 'throbbing':
            start_onair(status)

api.add_resource(OnAir, '/onair/<status>')

if __name__ == '__main__':
     app.run(host= '0.0.0.0',port=80)
