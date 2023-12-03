import time
import creating_QA_model
# import match_rules
# import find_intent
# import qa_matching
import params
import name_management
import booking_process
import timetable
import check_personal_confirmation as p_confirm
import reply_booking_steps
import ask_start_booking
from joblib import load
import re
import random
from user import User
def main():
    this_user = User()
    userName = this_user.name
    stop = False
    qn_q= load('Qid_Q_dict')   #load params:qn_q
    q_a = load('QA_Dictionary') #load params:q_a
    replies = params.responses_usual
    movie_list_replies = params.responses_movie_list
    print("Hi, I am a movie ticket booking assistant. Feel free to ask me some question or start booking a movie ticket.")
    while not stop:
        user_input = input(" (type anything to ask me, or enter 'stop' to quit) :")
        if user_input.lower() == 'stop':
            print("Goodbye!")
            stop = True
        # response = match_rules.send_message(user_input)
        else:
            # response = find_intent.respond(user_input)          
            # _intent = creating_QA_model.answer(user_input)
            if re.search('small*|Pricing*|Payment*|Location*|identity',creating_QA_model.answer(user_input)):
                _intent = creating_QA_model.answer(user_input)
            else:
                _intent = creating_QA_model.answer_clf(user_input)
            print(f"find intent by classifier : {creating_QA_model.answer_clf(user_input)}")
            print(f"find intent by similariity: {creating_QA_model.answer(user_input)}")   #for debugging
            if _intent =="initiate":
                name_management.askName(this_user)               
                response = random.choice(replies['greet'])
                print(response)
                time.sleep(2)
                print(random.choice(movie_list_replies))
            elif _intent =="identity management":
                name_management.replyName(this_user)
                time.sleep(2)
                print(random.choice(movie_list_replies))
            elif re.search('small*|Pricing*|Payment*|Location*',_intent) :  #response answer for Question and small talk
                response = random.choice(q_a[qn_q[_intent]])
                print(response)
            elif _intent =="Decide movie":
                booking_process.booking(this_user)
            elif _intent =="discoverability":
                response = random.choice(replies[_intent]) + random.choice(movie_list_replies)
                print(response)
            elif _intent =="Movie Listings":
                response = random.choice(movie_list_replies)
                print(response)
                ask_start_booking(this_user)
            elif _intent =="Movie Time":
                timetable.which_timetable(this_user)
            elif _intent =="Booking Process":
                reply_booking_steps.reply()
                ask_start_booking(this_user)
            elif _intent =="Seat Availability":
                response = f"I know your intent is {_intent}"
                print(response)
            elif _intent =="Confirmation":
                p_confirm.booked_details(this_user)      
            elif _intent == 'default': #defualt reply
                response = random.choice(replies[_intent])
                print(response)



if __name__ == "__main__":
    main ()