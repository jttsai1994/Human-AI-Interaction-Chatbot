# import process
import create_intent_model
import creating_QA_model
import match_rules
import find_intent
import match_intent
import qa_matching
import name_management
def main():
    userName = None
    stop = False
    while not stop:
        print(f"userName is {userName}")
        user_input = input(" (type anything to ask me, or enter 'stop' to quit) :")
        if user_input.lower() == 'stop':
            print("Goodbye!")
            stop = True
        # response = match_rules.send_message(user_input)
        else:
            # response = find_intent.respond(user_input)          
            _intent = match_intent.match_intent(user_input)

            if _intent =="initiate":
                userName = name_management.askName(userName)
                response = f"Nice to meet you! {userName}"
            elif _intent =="identity management":
                userName = name_management.replyName(userName)
                response = f"{userName}, What can I do for you"
            elif _intent == "default":
                response = qa_matching.answer(user_input)
            print(response)



if __name__ == "__main__":
    main ()