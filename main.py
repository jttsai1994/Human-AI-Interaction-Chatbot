# import process
# import create_intent_model
import creating_QA_model
# import match_rules
# import find_intent
# import qa_matching
import name_management
from joblib import load
import re
import random
def main():
    userName = None
    stop = False
    qn_q= load('Qid_Q_dict')   #load params:qn_q
    q_a = load('QA_Dictionary') #load params:q_a
    while not stop:
        print(f"userName is {userName}")
        user_input = input(" (type anything to ask me, or enter 'stop' to quit) :")
        if user_input.lower() == 'stop':
            print("Goodbye!")
            stop = True
        # response = match_rules.send_message(user_input)
        else:
            # response = find_intent.respond(user_input)          
            _intent = creating_QA_model.answer(user_input)
            print(f"return intent from creating_QA_model.answer : {_intent}")   #for debugging
            if _intent =="initiate":
                userName = name_management.askName(userName)
                response = f"Nice to meet you! {userName}"
            elif _intent =="identity management":
                userName = name_management.replyName(userName)
                response = f"{userName}, What can I do for you"
            elif re.search('Q*',_intent)[0] :  #response answer
                response = random.choice(q_a[qn_q[_intent]])
            elif _intent == 'defualt': #defualt reply
                response = "Sorry I can not understand. Can you give me more details?"
            print(response)



if __name__ == "__main__":
    main ()