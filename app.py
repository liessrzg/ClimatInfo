from flask import Flask, render_template, request, jsonify
import requests
from geopy.geocoders import Nominatim

app = Flask(__name__)

API_KEY = '5a7dfc23cc8164cd543e59dbeb9d1852'

def get_weather_data(city=None, lat=None, lon=None):
    if city:
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    elif lat and lon:
        url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    else:
        return None
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    data = request.json
    city = data.get('city')
    lat = data.get('lat')
    lon = data.get('lon')
    weather_data = get_weather_data(city=city, lat=lat, lon=lon)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
