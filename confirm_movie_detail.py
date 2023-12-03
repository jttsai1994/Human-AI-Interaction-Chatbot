import re
import time
import booking_process
import change_booking
def ask_to_confirm(user):
    time.sleep(1)
    print(f"You chose to watch :{user.movie.upper()} on {user.visitDate} {user.visitTime}")
    time.sleep(1)
    _ans = input("Do you want to book a movie with these detail? (Y/N):")
    if re.search('y*',_ans.lower())[0]:
        user.confirm_ok()
        print("OK, let's move on to the next step.")
    else:
        change_booking.lets_change_booking(user)  