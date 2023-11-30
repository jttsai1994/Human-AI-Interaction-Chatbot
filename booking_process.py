import re
import params
def booking(user):
    movie_pattern = "|".join(params.movie_list).lower()
    stop = False
    while not stop:
        if not user.movie:
            print("Seems like you haven't choose a movie to watch")
            user_ans= input("What do you want to watch? :")
            if re.search(movie_pattern,user_ans.lower()):
                user_movie = re.search(movie_pattern,user_ans.lower())[0]
                user.target_movie(user_movie)
                print(f"OK, we will choose {user_movie} for you")
            else:
                print(f"Sorry, we can't arrange with your answer.")
        else:
            print(f"Seems like you are interested in watching {user.movie}")

        if not user.visitDate:
            pass
        
        elif not user.visitTime:
            pass

        elif not user.payMethod:
            pass

        elif not user.confirm:
            pass
        
        


        user_input = input(" (enter 'stop' to quit) :")
        if user_input.lower() == 'stop':
            print("Goodbye!")
            stop = True
        # response = match_rules.send_message(user_input)
        