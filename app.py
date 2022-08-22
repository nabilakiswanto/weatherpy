
from flask import Flask, request, render_template, abort, Response

import json
import urllib
import math

app = Flask(__name__)

@app.route("/", methods=["GET"])
def round_decimals_up(number:float, decimals:int=2):
    """
    Returns a value rounded up to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.ceil(number)

    factor = 10 ** decimals
    return math.ceil(number * factor) / factor
def index():
    city = request.args.get('city')
    
    if city is None:
        abort(400, 'Tambahkan argument nama kota pada url example: 127.0.0.1:5000/?city=manado(replace with ur desired city)')

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
    return render_template('index.html', title='Weather App - Flask', round=round_decimals_up, data=json.loads(data.read().decode('utf8')))

if __name__ == "__main__":
    app.run()