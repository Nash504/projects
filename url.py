import hashlib
from colorama import Fore
def shorten(url):
    hash=hashlib.md5(url.encode())
    short=hash.hexdigest()
    return short

if __name__=='__main__':
    url=input("Enter the url to be shortened")
    short=shorten(url)
    print(Fore.GREEN+"The shortened url:"+Fore.CYAN+short)