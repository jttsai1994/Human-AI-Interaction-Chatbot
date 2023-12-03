import re
import time
import booking_process
import change_booking
def ask_to_confirm(user):
    print(f"You chose to watch :{user.movie.upper()} on {user.visitDate} {user.visitTime}")
    _ans = input("Do you want to book a movie with these detail? (Y/N):")
    if re.search('y*',_ans.lower())[0]:
        print("OK, let's start the booking process")
        time.sleep(1)
        booking_process.booking(user)
    else:
        change_booking.lets_change_booking(user)  