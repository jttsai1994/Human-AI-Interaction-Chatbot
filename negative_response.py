import time
import find_qa
import random
import params
def ask(user):
    leave = False
    intent ={
        1:"Movie Listings",2:"Movie Time",
        3:"Decide movie",4:"Confirmation",
        5:"discoverability",6:"identity management"
    }
    choosing_String= """
    Which topic are you asking? 
    (Please type in a NUMBER from 1~6)
    1. What's on
    2. Movie timetable
    3. Start a booking
    4. Confirm your booking
    5. What can the chatbot do
    6. Asking the bot for knowing the username
"""
    print(params.responses_usual['negative'])
    while not leave:
        try:
            ans_index = input(f"{choosing_String}")
            if int(ans_index) in list(range(1,7)):
                return intent(int(ans_index))
            else:
                print(f"Sorry, we can't arrange with your answer.")
                time.sleep(2)
                decide_yet = input("Are you asking for information about theatre location, ticket price or payment method (Y/N): ")
                if 'n' in decide_yet.lower():
                    print("Sorry I can't help you this time. I will improve in the future.")
                    leave = True      
                else:
                    leave = find_qa.ask()
        
        except:
                print(f"Sorry you must type in an number within {list(range(1,7))}")
                time.sleep(2)
                decide_yet = input("Are you asking for information about theatre location, ticket price or payment method (Y/N): ")
                if 'n' in decide_yet.lower():
                    print("Sorry I can't help you this time. I will improve in the future.")
                    leave = True      
                else:
                    leave = find_qa.ask()