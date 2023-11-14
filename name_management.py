import random
def askName(userName,firstTime=1):
    if not userName:
        if firstTime:
            userName = input("Hi! Please tell me your name: ")
        else:
            userName = input("Sorry I don't know your name yet, please tell me: ")
        return userName
    else: #if bot already know userName but the user's intent as "initiate"
        replyName(userName)
    
def replyName(userName):
    reply = [f"I know you are {userName}",
             f"Nice to hear from you again! {userName}",
             f"Everyone knows you are {userName}"]
    if not userName: # if user has not been asked for Name
        askName(0)
    else:
        print (random.choice(reply))
        return userName
