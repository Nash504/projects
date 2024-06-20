import json
import requests
from pywebio.input import *                     #API KEY:0bf2e845d85b8f224bc3813a747ae4b8
from pywebio.output import *
from pywebio.session import *
API_KEY="0bf2e845d85b8f224bc3813a747ae4b8"
def get_weather(city_name):
    clear()
    put_html("<h1 style='color:Blue;' >Weather Application</h1>")
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    complete_url=base_url+"q="+city_name+"&appid="+API_KEY+"&units=metric"
    response=requests.get(complete_url)#permission
    data=response.json()#actually getting it buts in all fluff
    print(data["weather"][0]["description"])#the good stuff
    if data["cod"] != "404":
        temperature = data["main"]["feels_like"]
        city = data["name"]
        weather_description = data["weather"][0]["description"]

        if temperature < 15:
            color = "cyan"
        elif 15 <= temperature <= 25:
            color = "green"
        else:
            color = "red"

        report = f"""
        <p><b>City:</b> <span style='font-weight:bold;'>{city}</span></p>
        <p><b>Weather:</b> <span style='font-weight:bold;'>{weather_description}</span></p>
        <p><b>Temperature:</b> <span style='color:{color}; font-weight:bold;'>{temperature}°C</span></p>
        """
        
        put_html(report)
if __name__=="__main__":
    while True:
        #put_html("<h1 style='color:Blue;' >Weather Application</h1>")
        p=input("City Name")
        get_weather(p)
    hold()






     
