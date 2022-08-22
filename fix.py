from xmlrpc.client import DateTime
from flask import Flask, request, render_template,json
import requests

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])

def index():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    weatherData = ''
    error = 0
    cityName = ''
    if request.method == "POST": 
        cityName = request.form.get("cityName")
        weatherApiKey = 'bafa0c89b1cda79638c2bab4713670ce'
        url="https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid=" + weatherApiKey
        weatherData=requests.get(url).json()
        
    return render_template('fix.html',title='Weatherapy - Flask',time=current_time, data = weatherData, cityName = cityName, error = error)

if __name__ == "__main__":
    app.run()