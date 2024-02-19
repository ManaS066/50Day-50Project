import random
from art import logo
print(logo)
num=random.randrange(100)
def guess(x):
    
    while x >0 :
        guess=int(input("enter the number :"))
        if num == guess:
            print("you won you guess the right num :",num)
            break
        elif num>guess:
            if num-guess >10:
                print("too high")
                
            else :
                print("little high")
                
        elif guess>num :
            if guess-num >10 :
                print("too low")
                
            else :
                print("littl low")          
        x-=1
        print("Remaining attempt is :",x)
x=input("If you want to continue then press 'y' otheswise 'n' : ")
if x=='y':
    level=input("enter your level of game 'easy' or 'hard' :")
    if level=='easy':
        print("You have chose easy level you have10 attempts .")
        guess(10)
    elif level=='hard':
        guess(5)
        print("You have chose easy level you have10 attempts .")

    else :
        print("Invalid input !! ")

