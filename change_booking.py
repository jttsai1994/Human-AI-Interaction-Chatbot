import re
import booking_process
import random

def lets_change_booking(user):
    user.confirm_reset()
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