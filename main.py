# import process
import match_rules
import find_intent
import match_intent
import qa_matching
def main():
    stop = False
    while not stop:
        user_input = input(" (type anything to ask me, or enter 'stop' to quit) :")
        if user_input.lower() == 'stop':
            print("Goodbye!")
            stop = True
        # response = match_rules.send_message(user_input)
        else:
            # response = find_intent.respond(user_input)          
            response = match_intent.match_intent(user_input)
            if response == "default":
                response = qa_matching.answer(user_input)
            print(response)



if __name__ == "__main__":
    main ()