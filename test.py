from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def index():
    weatherData = ''
    error = 0
    cityName = ''
    if request.method == "POST": 
        cityName = request.form.get("cityName")
        weatherApiKey = 'bafa0c89b1cda79638c2bab4713670ce'
        url="https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid=" + weatherApiKey
        weatherData=requests.get(url).json()
        
    return render_template('index.html', data = weatherData, cityName = cityName, error = error)

if __name__ == "__main__":
    app.run()