from params import movie_list
import re
import random
from params import responses_movie_list
import params
def ask_which_movie(user):
    movie_pattern = "|".join(movie_list).lower()
    leave = False
    while not (user.movie or leave):
        if not user.movie:
            print(random.choice(responses_movie_list))
            print("Seems like you haven't choose a movie to watch")
            user_ans= input("What do you want to watch? :")
            if re.search(movie_pattern,user_ans.lower()):
                user_movie = re.search(movie_pattern,user_ans.lower())[0]
                user.target_movie(user_movie)
                print(f"OK, we will choose {user_movie} for you")
            else:
                print(f"Sorry, we can't arrange with your answer.")
                decide_yet = input("Have you decided which movie? (Y/N): ")
                if 'n' in decide_yet.lower():
                    leave = True
        else:
            print(f"Seems like you are interested in watching {user.movie}")
    
