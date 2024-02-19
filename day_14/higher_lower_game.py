from art import *
import random
from data import data
import os
cls=lambda:os.system('cls')
a=random.choice(data)
b=random.choice(data)
score=0
def retry(a,b,score):
    a=b
    b=random.choice(data)
    dis(a,b,score)

def calculate(a,b,choice,score):  
    flag=0
    f_a=int(a['follower_count'])
    f_b =int(b['follower_count'])
    while flag ==0 :
        if choice=='a':
            if  f_a>f_b :
                print("you won")
                score+=10
                print(score,': is your current score in a')
                retry(a,b,score)
            elif f_b>f_a :
                print('you loose by selecting a')
                flag=1
                break
        elif choice=='b':
            if f_b > f_a:
                print("you won")
                score+=10
                print(score,': is your current score in b')
                retry(a,b,score)
            elif f_a>f_b :
                print('you loose by selecting b')
                flag=1
                break
print(logo)
def dis(a,b,score):
    print(f'Compare A : {a['name'] } , {a['description']} from :{a['country']} ')
    print(vs)
    print(f'Compare B : {b['name'] } , {b['description']} from :{b['country']} ')
    choice=input(f"Who has more follower type 'a' for {a['name']} or type 'b' for {b['name']} :")
    calculate(a,b,choice,score)
dis(a,b,score)