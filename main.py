import process
import functions
def main():
    while True:
        user_input = input(" (type anything to ask me, or enter 'exit' to quit) :")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = functions.send_message(user_input)
        print(response)



if __name__ == "__main__":
    main ()