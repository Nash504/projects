import time
from colorama import Fore,Style,init
init(autoreset=True)
def countdown(t):
    while t:
        min,sec=divmod(t,60)
        timer="{:02d}:{:02d}".format(min,sec)
        print(Fore.GREEN+timer,end='\r')
        time.sleep(1)
        t-=1
    print(Fore.CYAN+"Times up!")
t=int(input(Fore.BLUE+"Enter the seconds:"))
countdown(t)
