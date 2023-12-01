# import process
# import create_intent_model
import creating_QA_model
# import match_rules
# import find_intent
# import qa_matching
import params
import name_management
import booking_process
import timetable
import check_personal_confirmation as p_confirm
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
    while not stop:
        user_input = input(" (type anything to ask me, or enter 'stop' to quit) :")
        if user_input.lower() == 'stop':
            print("Goodbye!")
            stop = True
        # response = match_rules.send_message(user_input)
        else:
            # response = find_intent.respond(user_input)          
            # _intent = creating_QA_model.answer(user_input)
            _intent = creating_QA_model.answer_clf(user_input)
            print(f"find intent by classifier : {creating_QA_model.answer_clf(user_input)}")
            print(f"find intent by similariity: {creating_QA_model.answer(user_input)}")   #for debugging
            if _intent =="initiate":
                userName = name_management.askName(userName)
                this_user.set_name(userName)
                response = random.choice(replies['greet'])
            elif _intent =="identity management":
                userName = name_management.replyName(userName)
                response = f"{userName}, Which movie you want to watch in our cinema?"
            elif re.search('small*|Pricing*|Payment*|Location*',_intent) :  #response answer for Question and small talk
                response = random.choice(q_a[qn_q[_intent]])
            elif _intent =="Decide movie":
                response = f"I know your intent is {_intent}" 
                booking_process.booking(this_user)
            elif _intent =="discoverability":
                response = random.choice(replies[_intent]) + random.choice(movie_list_replies)
            elif _intent =="Movie Listings":
                response = random.choice(movie_list_replies)
                booking_process.booking(this_user)
            elif _intent =="Movie Time":
                response = f"I know your intent is {_intent}" 
                timetable.which_timetable(this_user)
            elif _intent =="Booking Process":
                response = f"I know your intent is {_intent}"
            elif _intent =="Seat Availability":
                response = f"I know your intent is {_intent}" 
            elif _intent =="Confirmation":
                response = f"I know your intent is {_intent}" 
                p_confirm.booked_details(this_user)      
            elif _intent == 'default': #defualt reply
                response = random.choice(replies[_intent])
            print(response)



if __name__ == "__main__":
    main ()