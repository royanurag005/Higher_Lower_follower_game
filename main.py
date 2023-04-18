from game_data import data
import art
import random
from replit import clear
SCORE=0
user_A=random.choice(data)
user_B=random.choice(data)

def print_logo():
    print(art.logo)
def choice_of_user():
    print_logo()
    global user_A,user_B
    user_A=random.choice(data)
    user_B=random.choice(data)
    while(user_A==user_B):
        user_B=random.choice(data)

        
def new_origins():
    global data
    global user_A,user_B
    if(user_A['follower_count']>=user_B['follower_count']):
        data.remove(user_B)
        user_B=random.choice(data)
    elif(user_B['follower_count']>=user_A['follower_count']):
        data.remove(user_A)
        user_A=user_B
        
        user_B=random.choice(data)
    # global Game_over
    # Game_over=False

        
# def user_display():
# print(f"Compare A : {} , a {} , from {}")
def print_user_info():
    print(f"Compare A : {user_A['name']}, a {user_A['description']}, from {user_A['country']}.")
    print(art.vs)
    print(f"Compare B : {user_B['name']}, a {user_B['description']}, from {user_B['country']}.")

def follower_check():
    
    entry=input("Who has more followers? Type 'A' or 'B':").upper()
    clear()
    print_logo()
    if(entry=='A'):
        if(user_A['follower_count']>=user_B['follower_count']):
            global SCORE
            SCORE=SCORE+1
            print(f"You're right! Current Score : {SCORE}.")
            new_origins()
        else:
            print(f"Sorry. that's wrong. Final score : {SCORE}")
            global Game_over
            Game_over=True
    elif(entry=='B'):
        if(user_B['follower_count']>=user_A['follower_count']):
            SCORE
            SCORE=SCORE+1
            print(f"You're right! Current Score : {SCORE}.")
            new_origins()
        else:
            print(f"Sorry. that's wrong. Final score : {SCORE}")
            Game_over
            Game_over=True
    else:
        print("Wrong Entry")
        Game_over
        Game_over=True
Game_over=False
choice_of_user()
while not Game_over:


    print_user_info()
    follower_check()
    new_origins()
print("Thank You!!!")  
    
