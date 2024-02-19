import os
from art import logo
print(logo)
cls = lambda: os.system('cls')
def bid(info):
    name=input("enter your name :")
    amt=int(input("enter your bid :"))
    info[name]=amt
    cls()
info={}
bid(info)
while True:
    dir=input("enter 'yes' if another bidder is present othewise 'no' :").lower()
    if dir=='yes':
        True
        bid(info)
    else:
       v = list(info.values())
       k = list(info.keys())
       max_bid=k[v.index(max(v))]
       print (f"The maximum bid is given by {max_bid} !! CONGRATULATION !!") 
       break