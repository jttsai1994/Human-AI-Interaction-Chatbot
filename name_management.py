import random
def askName(userName,from_name_managment=0):
    if not userName:
        if not from_name_managment:
            userName = input("Hi! Please tell me your name: ")
        else:
            userName = input("Sorry I don't know your name yet, please tell me: ")
        return userName
    else: #if bot already know userName but the user's intent as "initiate"
        return replyName(userName)
    
def replyName(userName):
    reply = [f"I know you are {userName}",
             f"Nice to hear from you again! {userName}",
             f"Everyone knows you are {userName}"]
    if not userName: # if user has not been asked for Name
        return askName(userName,from_name_managment=1)
    else:
        print (random.choice(reply))
        return userName
