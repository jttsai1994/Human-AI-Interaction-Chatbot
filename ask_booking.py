import re
import booking_process
import random
from params import responses_movie_list
def start_booking(user):
    print("I can help you to start/finish your booking")
    print("All you have to do is decide: Movie/ Visit Date/ Visit Time/ Payment Method")
    print("Seems like you have not made any movie ticket reservation")
    print(random.choice(responses_movie_list))
    _ans = input("Would you like to book a movie ticket right away? (Y/N):")
    if re.search('y*',_ans.lower())[0]:
        booking_process.booking(user)
    else:
        print("You still have time to make a decision! No worries!") 