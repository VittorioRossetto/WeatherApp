import config
from flask import Flask, render_template, request, redirect
import json
import requests
import urllib.request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        country = request.form['country']
        api_key = config.api_key

        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}')

        weather_data = weather_url.json()

        try:
            description = str(weather_data['weather'][0]['description'])
            temp = round(weather_data['main']['temp']) - 273
            humidity = weather_data['main']['humidity']
            wind = weather_data['wind']['speed']
            return render_template("result.html", temp=temp, humidity=humidity, wind=wind, city=city, description=description)
        except:
            return 'There was an issue with your location'

    return render_template("index.html")

@app.route('/result/<int:id>')
def result():
    if request.method == 'POST':
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)