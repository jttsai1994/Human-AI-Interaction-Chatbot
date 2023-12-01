import random
def askName(user,from_name_managment=0):
    if not user.name:
        if not from_name_managment:
            userName = input("Hi! Please tell me your name: ")
        else:
            userName = input("Sorry I don't know your name yet, please tell me: ")
        user.set_name(userName)
        return user.name
    else: #if bot already know userName but the user's intent as "initiate"
        return replyName(user.name)
    
def replyName(user):
    reply = [f"I know you are {user.name}",
             f"Nice to hear from you again! {user.name}",
             f"Everyone knows you are {user.name}"]
    if not user.name: # if user has not been asked for Name
        return askName(user,from_name_managment=1)
    else:
        print (random.choice(reply))
        return user.name
