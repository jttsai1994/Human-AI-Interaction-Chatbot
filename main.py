import time
import creating_QA_model
from params import responses_movie_list
import params
import name_management
import booking_process
import timetable
import check_personal_confirmation as p_confirm
import reply_booking_steps
import ask_start_booking
import negative_response
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
    print(random.choice(replies["discoverability"]) )
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
            # print(f"find intent by classifier : {creating_QA_model.answer_clf(user_input)}")
            # print(f"find intent by similariity: {creating_QA_model.answer(user_input)}")   #for debugging
            if _intent =="Negative response":
                actual_intent = negative_response.ask(this_user)
                if actual_intent:
                    _intent = actual_intent
                    print(_intent)
                else:
                    pass
            if _intent =="initiate":
                name_management.askName(this_user)               
                print(f"Hey {this_user.name}! "+random.choice(replies['greet']))
                time.sleep(2)
                print(random.choice(responses_movie_list))
            elif _intent =="identity management":
                name_management.replyName(this_user)
                time.sleep(2)
                print(f"Hi {this_user.name}!"+random.choice(replies['greet']))
                print(random.choice(responses_movie_list))
            elif re.search('small*|Pricing*|Payment*|Location*',_intent) :  #response answer for Question and small talk
                response = random.choice(q_a[qn_q[_intent]])
                print(response)
            elif _intent =="Decide movie":
                booking_process.booking(this_user)
            elif _intent =="discoverability":
                print(random.choice(replies[_intent]) )
                time.sleep(2)
                print(random.choice(responses_movie_list))
            elif _intent =="Movie Listings":
                print(random.choice(responses_movie_list))
                ask_start_booking.ask(this_user)
            elif _intent =="Movie Time":
                timetable.which_timetable(this_user)
            elif _intent =="Booking Process":
                reply_booking_steps.reply()
                print(random.choice(responses_movie_list))
                ask_start_booking.ask(this_user)
            elif _intent =="Positive response":
                print(random.choice(replies["thankyou"]) )
            elif _intent =="Confirmation":
                p_confirm.booked_details(this_user)      
            elif _intent == 'default': #defualt reply
                response = random.choice(replies[_intent])
                print(response)



if __name__ == "__main__":
    main ()