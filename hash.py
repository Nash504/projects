import hashlib;
from colorama import Fore,Style,init;
init( autoreset=True)
def hashtext(text,algo):
    if algo.lower() not in list:
        return False
    h=hashlib.new(algo)
    h.update(text.encode())
    return h.hexdigest()
list=['shake_256', 'sha3_512', 'sha384', 'md5', 'sha512', 'blake2s', 'sha3_256', 'shake_128', 'sha3_224', 'blake2b', 'sha1', 'sha256', 'sha224', 'sha3_384']
while True:
    p=input(Fore.LIGHTCYAN_EX+"Enter the text to be hashed:")
    for i in list:
      print(Fore.YELLOW+i,end="\n")
    algo=input(Fore.RED+"Please select an algorithm for hashing:")
    ans=hashtext(p,algo.lower())
    if ans:
      print(Fore.GREEN+"Hashed text:"+ans)
    else:
      print(Fore.LIGHTRED_EX+"Invalid algo selected")

    
