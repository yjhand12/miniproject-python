from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"
API_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET','POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            params = {
                'q': city,
                'appid' : API_KEY,
                'units' : 'metric'
            }
            response = requests.get(API_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                weather_data = {'error': 'City not found'}
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)