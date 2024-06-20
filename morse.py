from colorama import Fore,init,Style;
import time;
init(autoreset=True)
morse_code_dict = {
	'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
	'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
	'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
	'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
	'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
	'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
	'Y': '-.--', 'Z': '--..',
	'0': '-----', '1': '.----', '2': '..---',
	'3': '...--', '4': '....-', '5': '.....',
	'6': '-....', '7': '--...', '8': '---..', '9': '----.',' ':'/'
}
def encrypt(text):
  text = text.upper()
  morse=''
  for i in text:
    morse+= morse_code_dict[i]
    morse+='   '
  return morse
def decrypt(morse):
 text=" "
 morse=morse.split(' ')
 for i in morse:
   for j in morse_code_dict:
     if morse_code_dict[j]==i:
       text+=j
 return text
  
  
while True:
  print(Fore.BLUE+"----MENU-----")
  print(Fore.CYAN+"  1.DECRYPT")
  print(Fore.YELLOW+" 2.ENCRYPT")
  print(Fore.RED+"  3.EXIT")
  choice = input("Enter your choice: ")
  if choice == '2':
    text=input("Enter the text to encrypt to morse code:")
    morse_code=encrypt(text)
    print(Fore.GREEN+"MORSE CODE:"+morse_code)
    time.sleep(2)
  elif choice =='1':
    morse_code=input("Enter the morse code to be converted:")
    text=decrypt(morse_code)
    print(Fore.GREEN+"DECRYPTED TEXT:"+text)
    time.sleep(2)
  elif choice =='3':
     print(Fore.RED+"Exiting...")
     break
  

      