import re
import booking_process
import random
from params import responses_movie_list
def booked_details(user):
    if user.movie:
        change_booking = False
        msg= f''' 
    Hello {user.name}, you will watch {user.movie} on {user.visitDate} / {user.visitTime}
    '''
        print(f'{msg}')
        _ans = input('Do you want to change your booking? (Y/N) : ')
        if re.search('y*',_ans.lower())[0]:
            change_booking = True
        else:
            print(f"Enjoy the movie {user.movie} on {user.visitDate}!")
        if change_booking:
            print('Which details you want to change? Movie, Date, or Time? ')
            _change =input('Please type 1 for Movie, 2 for Date, 3 for Time: ')
            if _change == '1':
                user.reset_all_booking_details()
                booking_process.booking(user)
            elif _change == '2':
                user.reset_visitDate()
                user.reset_visitTime()
                booking_process.booking(user)
            elif _change == '3':           
                user.reset_visitTime()
                booking_process.booking(user)
            else:
                print('sorry, because of the wrong input, you could not change booking details in this turn.')
    else:
        print("Seems like you have not made any movie ticket reservation")
        print(random.choice(responses_movie_list))
        _ans = input("Would you like to book a movie ticket right away? (Y/N):")
        if re.search('y*',_ans.lower())[0]:
            booking_process.booking(user)
        else:
            print("You still have time to make a decision! No worries!")


