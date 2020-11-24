from requests import get
from json import loads, dumps
from flask import Flask, Response
from os import sys
from colorama import Fore

args = sys.argv

def help():
    print(f"""
Manual for this app.

help          -h --help open help for app.
command Mode  -cmd [-ip<option>] --command [-ip<option>] run the app in command mode.
ip address    -ip<ip address> ip address.

To run in web api mode:
    RUN FOLLOWING COMMAND IN PWD
    $ export FLASK_APP=app.py
    $ flask run
""")

if('-h' in args or '--help' in args):
    help()

def res(data, status=200, indent=4, mimetype="application/json"):
    return Response(
        dumps(data, indent=indent), 
        mimetype=mimetype, 
        status=status
    )


def data(ip=None):
    try:
        ip_data = get(f"https://ipinfo.io/{ip if ip else ''}").text
        data = loads(ip_data)
        (lat, long) =  data["loc"].split(',') if data["loc"].split(',') else str(data).split(',')
        weather_data = get(f"https://fcc-weather-api.glitch.me/api/current?lat={lat}&lon={long}").text
        return res({
            **data,
            **loads(weather_data)
        })
    except Exception as e:
        return res({"error": str(e)})

if('-cmd' in args or '--command' in args):
    ip = None
    try:
       if '-ip' in args:
           ip = args[args.index('-ip') + 1]
    except Exception as e:
        pass
    print(data(ip).get_data(as_text=True))



app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/<ip>')
def root(ip=None):
    return data(ip)
