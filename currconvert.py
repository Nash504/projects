import requests
from pywebio.input import input
from pywebio.output import put_text, put_table, put_error, put_success
from pywebio import start_server

API_KEY = 'your_openweathermap_api_key'  # Replace with your OpenWeatherMap API key

def get_air_quality(city_name):
    try:
        url = f'http://api.openweathermap.org/data/2.5/air_pollution?'
        params = {
            'q': city_name,
            'appid': API_KEY
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            air_quality = data['list'][0]['main']['aqi']
            components = data['list'][0]['components']
            return air_quality, components
        else:
            return None, None
    except Exception as e:
        return None, None

def air_quality_app():
    city_name = input("Enter the city name:", required=True)
    air_quality, components = get_air_quality(city_name)
    
    if air_quality is None:
        put_error("Error fetching air quality data. Please check the city name and try again.")
    else:
        air_quality_levels = {
            1: 'Good',
            2: 'Fair',
            3: 'Moderate',
            4: 'Poor',
            5: 'Very Poor'
        }
        
        put_success(f'Air Quality in {city_name}: {air_quality_levels[air_quality]}')
        put_table([
            ['Component', 'Value (μg/m³)', 'Safe Level (μg/m³)', 'Health Effects'],
            ['CO', components['co'], '9 (ppm)', 'High levels can reduce oxygen in the bloodstream.'],
            ['NO2', components['no2'], '40', 'Can irritate the airways and decrease lung function.'],
            ['O3', components['o3'], '100', 'Can cause chest pain, coughing, and airway inflammation.'],
            ['SO2', components['so2'], '20', 'Can cause respiratory problems and heart disease.'],
            ['PM2.5', components['pm2_5'], '25', 'Can cause cardiovascular and respiratory issues.'],
            ['PM10', components['pm10'], '50', 'Can cause respiratory issues and reduce lung function.']
        ])

if __name__ == '__main__':
    start_server(air_quality_app, port=8080)
