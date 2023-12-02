import re
import booking_process
import random
from params import responses_movie_list
import time
import change_booking
def start_booking(user):
    print("I can help you to start/finish your booking")
    time.sleep(1)
    print("All you have to do is decide: Movie/ Visit Date/ Visit Time/ Payment Method")
    time.sleep(1)
    # if the user has not decide a movie -> ask if the user want to star booking
    if not user.movie:
        print("Seems like you have not made any movie ticket reservation")
        time.sleep(1)
        print(random.choice(responses_movie_list))
        _ans = input("Would you like to book a movie ticket right away? (Y/N):")
        if re.search('y*',_ans.lower())[0]:
            print("OK, let's start the booking process")
            time.sleep(1)
            booking_process.booking(user)
        else:
            print("You still have time to make a decision! No worries!")
    else: #if the user already decided a movie -> ask if the user want to change
        wanna_change = False
        if user.name:
            msg= f''' 
Hello {user.name}, you will watch {user.movie.upper()} on {user.visitDate} / {user.visitTime}
        '''
        else:
            msg= f''' 
You will watch {user.movie.upper()} on {user.visitDate} / {user.visitTime}
        '''
        print(f'{msg}')
        _ans = input('Do you want to change your booking? (Y/N) : ')
        if re.search('y*',_ans.lower())[0]:
            wanna_change = True
        else:
            print(f"Enjoy the movie {user.movie} on {user.visitDate}!")
        if wanna_change:
            change_booking.lets_change_booking(user)       