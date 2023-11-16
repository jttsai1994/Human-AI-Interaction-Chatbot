# import process
# import create_intent_model
import creating_QA_model
# import match_rules
# import find_intent
# import qa_matching
import params
import name_management
from joblib import load
import re
import random
def main():
    userName = None
    stop = False
    qn_q= load('Qid_Q_dict')   #load params:qn_q
    q_a = load('QA_Dictionary') #load params:q_a
    replies = params.responses_usual
    while not stop:
        user_input = input(" (type anything to ask me, or enter 'stop' to quit) :")
        if user_input.lower() == 'stop':
            print("Goodbye!")
            stop = True
        # response = match_rules.send_message(user_input)
        else:
            # response = find_intent.respond(user_input)          
            _intent = creating_QA_model.answer(user_input)
            # print(f"return intent from creating_QA_model.answer : {_intent}")   #for debugging
            if _intent =="initiate":
                userName = name_management.askName(userName)
                response = random.choice(replies['greet'])
            elif _intent =="identity management":
                userName = name_management.replyName(userName)
                response = f"{userName}, What can I do for you"
            elif re.search('small*|Q*',_intent)[0] :  #response answer for Question and small talk
                response = random.choice(q_a[qn_q[_intent]])
            elif _intent =="discoverability":
                response = random.choice(replies[_intent])          
            elif _intent == 'default': #defualt reply
                response = random.choice(replies[_intent])
            print(response)



if __name__ == "__main__":
    main ()