import random
import time
from colorama import Fore, Style, init
init(autoreset=True)
# Set of tools
a = {"Rock", "Paper", "Scissor"}
u_score = 0
c_score=0
easter = 0

print(Fore.RED+"These are your tools:")
for i in a:
    print(Fore.CYAN+i)
print(Fore.BLUE+"Get ready to face off!!")

while u_score != 3 and c_score!=3:
    time.sleep(2)
    user_ch = input(Fore.BLUE+"Choose your option \o/--->> ")
    
    if user_ch not in a and easter == 0:
        print(Fore.RED+"Pick a valid option")
        easter += 1
        continue
    
    if user_ch not in a and easter == 1:
        print(Fore.RED+"Wrong Option Again Amigo haha")
        easter += 1
        continue
    
    if user_ch not in a and easter == 2:
        print(Fore.RED+"Seriously?")
        easter += 1
        continue
    
    if user_ch not in a and easter == 3:
        print(Fore.RED+"Last Chance Bub")
        easter += 1
        continue
    if user_ch not in a and easter==4:
        print(Fore.YELLOW+"Fuck you loser -_-")
        break
    
    # If the input is valid, get the computer's choice
    comp_ch = random.choice(list(a))
    print(f"Computer choice: {comp_ch}")
    if user_ch=="Rock" and comp_ch=="Paper":
        print("Paper covers Rock, you lose :")
        c_score+=1
    elif user_ch=="Rock" and comp_ch=="Scissor":
        print("Rock crushes Scissor, you win!")
        u_score += 1
    elif user_ch=="Scissor" and comp_ch=="Paper":
        print("Scissor cuts Paper, you win!")
        u_score += 1
    elif user_ch=="Scissor" and comp_ch=="Rock":
        print("Rock crushes Scissor, you lose :")
        c_score += 1
    elif user_ch=="Paper" and comp_ch=="Rock":
        print("Paper covers Rock, you win!")
        u_score += 1
    elif(user_ch=="Scissor" and c_score=="Scissor"):
        print("Tie -_-")
    elif(user_ch=="Rock" and c_score=="Rock"):
        print("Tie -_-")
    elif(user_ch=="Paper" and c_score=="Paper"):
        print("Tie -_-")
    elif(user_ch=="Paper" and comp_ch=="Scissor"):
        print("Scissor cuts Paper, you lose :")
        c_score += 1

if u_score==3:
    print(Fore.GREEN+"Ya won!!!")

if c_score==3:
    print(Fore.RED+"Womp Womp better luck next time f@t@a$$")
       

if(easter==4):
    print(Fore.GREEN+"Game Over(Retard ending congrats!)")
