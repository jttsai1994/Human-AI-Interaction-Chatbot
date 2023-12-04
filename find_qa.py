import time
import find_qa
import creating_QA_model
def ask(user):
#     ans_index = input(f"""
#     Which topic are you asking? 
#     (Please type in a NUMBER from 1~3)
#     1. Theatre location
#     2. Ticket Price
#     3. Payment method
# """)
    user_query = input("Can you ask your question again?")
    possible_q_id = creating_QA_model.find_QA(user_query)
    print(possible_q_id)
    return True