from art import logo, vs
from game_data import data
import random

play=True
counter=0
a=random.choice(data)
b=random.choice(data)

while play==True:
    morefollowers=0
    a_followers=a['follower_count']
    b_followers=b['follower_count']
    print(logo)
    print("Compare A: "+a['name']+", "+a['description']+", from "+a['country'])
    print(vs)
    print("Against B: "+b['name']+", "+b['description']+", from "+b['country'])
    choice_in=input("Type in A or B")
    if a_followers>b_followers:
        morefollowers=a_followers
        b=random.choice(data)
    else:
        morefollowers=b_followers
        a=random.choice(data)
    if choice_in=='A':
        choice_in=a_followers
    else:
        choice_in=b_followers
    if choice_in==morefollowers:
        counter=counter+1
        print("Yes, you chose the right one.")
        print(str(counter)+" is your score")
    else:
        print("Wrong choice, you lose")
        print("your score: "+str(counter))
        play=False

