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
    reply = ["I know you are {Name}","Nice to hear from you again! {Name}","Everyone knows you are {Name}"]
    if not userName: # if user has not been asked for Name
        askName(0)
    else:
        print (random.choice(reply).format(userName))
        return userName
