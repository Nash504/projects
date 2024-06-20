
import json,requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
def create_password(length):
    clear()
    put_html("<h1> Password Generator</h1>")
    api_url=f"https://api.api-ninjas.com/v1/passwordgenerator?length={length}"
    response=requests.get(api_url, headers={'X-Api-Key': 'ZH+fZzgrfbOclJuktL0DHg==J5T0OcE93umMFzj7'})
    data=response.json()
    style(put_text(data['random_password']), 'color:blue;font-size:40px')
    length = input("Enter the length of the password", type="number")
    put_buttons([dict(label='Generate', value='create_password', color='outline-success')], onclick=create_password)
if __name__=='__main__':
    put_html("<h1> Password Generator</h1>")
    length = input("Enter the length of the password", type="number")
    put_buttons([dict(label='Generate', value='create_password', color='outline-success')], onclick=create_password)  # Correct function reference
    hold()