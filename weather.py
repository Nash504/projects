from bs4 import BeautifulSoup;
from win10toast import ToastNotifier;
import requests;
import time;
n=ToastNotifier()
def get_data(url):
    r=requests.get(url)
    return r.text
html_data=get_data("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")
bs=BeautifulSoup(html_data,'html.parser')
#print(bs.prettify())
temp=bs.find_all("span",class_=" _-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
current_temp=str(temp)
result= "current_temp " + current_temp
n.show_toast("Weather update",result, duration = 10)