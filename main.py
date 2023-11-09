import process
def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
    processed_input = process(user_input)
    print(f"Bot: You said {processed_input}")



if __name__ == "__main__":
    main ()