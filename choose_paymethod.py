from params import movie_list
import re
import random
from params import responses_movie_list
import params
def ask_payment_method(user):
    movie_pattern = "|".join(movie_list).lower()
    leave = False
    while not (user.payMethod or leave):
        if not user.payMethod :
            print("Seems like you haven't choose a payment method.")
            user_ans= input("You can pay by card or cash. Which one would you like? :")
            if re.search('card',user_ans.lower()):
                pay_method = re.search('card',user_ans.lower())[0]
                user.pay_by(pay_method)
                print(f"OK, you will pay by {user.payMethod}.")
            elif re.search('cash',user_ans.lower()): 
                pay_method = re.search('cash',user_ans.lower())[0]
                user.pay_by(pay_method)
                print(f"OK, you should bring your confirmation code at the ticket counter and pay by cash before the movie start.")                
            else :
                print(f"Sorry, we can't arrange with your answer.")
                decide_yet = input("Have you decided which movie? (Y/N): ")
                if 'n' in decide_yet.lower():
                    leave = True
        else:
            print(f"Seems like you are interested in watching {user.movie}")
