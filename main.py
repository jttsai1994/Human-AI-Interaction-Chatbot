import process
import match_rules
import find_intent
def main():
    while True:
        user_input = input(" (type anything to ask me, or enter 'exit' to quit) :")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        # response = match_rules.send_message(user_input)
        response = find_intent.respond(user_input)
        print(response)



if __name__ == "__main__":
    main ()