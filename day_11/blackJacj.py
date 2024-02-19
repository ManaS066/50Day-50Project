import random
import os
from art import logo
print(logo)
cls = lambda: os.system('cls')
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card=[]
deler_card=[]
def draw_card(x):
    select=random.choice(cards)
    x.append(select)
    cards.append(select)
def score(x):
    sum=0
    for i in x :
        sum+=i
    return sum
def cal(user_sum,deler_sum):
    if(user_sum < 21 ):
        a=input("you want to insert a card press 'y' else 'n' ")
        if a=='y':
            draw_card(user_card)
            
            print(f'Your card is {user_card}')
            user_sum=score(user_card)
            #ch=input("If you want to show press yes or add another card press no ")
            cal(user_sum,deler_sum)
        elif user_sum > deler_sum:
                print(f"you won \n you score is {user_sum} and deler score is {deler_sum} and card indeler hand is {deler_card}")
        elif deler_sum < 21 and deler_sum > user_sum:
            print(f"deler won \n you score is {user_sum} and deler score is {deler_sum} and card indeler hand is {deler_card}")
        elif deler_sum >21:
            print(f"deler loose \n you score is {user_sum} and deler score is {deler_sum}  and card indeler hand is {deler_card}")
    else:
        print(f"You lose \n you score is {user_sum} and deler score is {deler_sum} and card indeler hand is {deler_card}")
while True:
    start=input("you want to continue to game press  'yes' otherwise no ")
    if start != 'yes':
        break
    else:
        cls()
        user_card=[]
        deler_card=[]
        draw_card(user_card)
        draw_card(user_card)
        draw_card(deler_card)
        draw_card(deler_card)
        user_sum=score(user_card)
        deler_sum=score(deler_card)
        print(f"your cards are {user_card}")
        print(f"deler card is {deler_card[1]}")
        cal(user_sum,deler_sum)