
from flask import Flask, request, render_template, abort, Response
import requests
import json
import urllib

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    city = request.args.get('city')
    
    if city is None:
        abort(400, 'Missing argument city')

    data = {}
    data['q'] = request.args.get('city')
    data['appid'] = 'bafa0c89b1cda79638c2bab4713670ce'
    data['units'] = 'metric'
    
    url_values = urllib.parse.urlencode(data)
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    full_url = url + '?' + url_values
    data = urllib.request.urlopen(full_url)

    resp = Response(data)
    resp.status_code = 200
    return render_template('index.html', title='Weather App', data=json.loads(data.read().decode('utf8')))

if __name__ == "__main__":
    app.run()