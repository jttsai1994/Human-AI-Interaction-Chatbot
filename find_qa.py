import time
import creating_QA_model
import params
import random
def ask(user):
#     ans_index = input(f"""
#     Which topic are you asking? 
#     (Please type in a NUMBER from 1~3)
#     1. Theatre location
#     2. Ticket Price
#     3. Payment method
# """)
    user_query = input("Can you ask your question again?")
    possible_answer = creating_QA_model.find_QA(user_query)
    print(possible_answer[0])
    time.sleep(2)
    satisfied = input("Are you satisfied with this response? (Y/N)")
    if 'n' in satisfied.lower():
        time.sleep(1)
        print("Sorry I can't help you this time. I will improve in the future.")
    else:
        time.sleep(1)
        print(random.choice(params.responses_usual["thankyou"]) )
    return True