import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fact(_):
    clear()
    put_html("<h1 style='color:green;'>Fun Fact Generator </h1>")  
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")#ask website for permission idk
    data = response.json()#reading inside it
    useless_fact = data['text']
    style(put_text(useless_fact), 'color:blue;font-size:40px')
    put_buttons([dict(label='Click Me', value='get_fact', color='outline-success')], onclick=get_fact)  # Correct function reference

if __name__ == '__main__':
    put_html("<h1 style='color:green;'>Fun Fact Generator</h1>")  # Corrected closing tag
    put_buttons([dict(label='Click Me', value='get_fact', color='outline-success')], onclick=get_fact)  # Correct function reference
hold()
