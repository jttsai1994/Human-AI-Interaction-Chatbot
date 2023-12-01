import re
import booking_process
import random
from params import responses_movie_list
import time
def start_booking(user):
    print("I can help you to start/finish your booking")
    time.sleep(1)
    print("All you have to do is decide: Movie/ Visit Date/ Visit Time/ Payment Method")
    time.sleep(1)
    print("Seems like you have not made any movie ticket reservation")
    time.sleep(1)
    print(random.choice(responses_movie_list))
    _ans = input("Would you like to book a movie ticket right away? (Y/N):")
    if re.search('y*',_ans.lower())[0]:
        booking_process.booking(user)
    else:
        print("You still have time to make a decision! No worries!") 