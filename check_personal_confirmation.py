import re
import booking_process
import random
from params import responses_movie_list
import change_booking
def booked_details(user):
    if user.movie:
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
    else:
        print("Seems like you have not made any movie ticket reservation")
        print(random.choice(responses_movie_list))
        _ans = input("Would you like to book a movie ticket right away? (Y/N):")
        if re.search('y*',_ans.lower())[0]:
            booking_process.booking(user)
        else:
            print("You still have time to make a decision! No worries!")


