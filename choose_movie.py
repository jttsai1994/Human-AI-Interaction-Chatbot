from params import movie_list
import re
import random
from params import responses_movie_list
import params
import time
def ask_which_movie(user):
    movie_pattern = "|".join(movie_list).lower()
    leave = False

    if not user.movie:
        print(random.choice(responses_movie_list))
        time.sleep(2)
        print("First, it seems like you haven't chosen a movie to watch")
        time.sleep(2)
        while not (user.movie or leave):
            try:
                user_ans= input(f"What do you want to watch? (within {list(range(1,len(movie_list)+1))}):")
                if int(user_ans) in list(range(1,len(movie_list)+1)):
                    interested_movie_index = int(user_ans)-1
                    user_movie = movie_list[interested_movie_index].lower()
                    user.target_movie(user_movie)
                    print(f"Got it! We will choose {user_movie.upper()} for you")
                    time.sleep(2)
                else:
                    print(f"Sorry, we can't arrange with your answer.")
                    time.sleep(2)
                    decide_yet = input("Have you decided which movie? (Y/N): ")
                    if 'n' in decide_yet.lower():
                        leave = True
            except:
                print(f"Sorry you must type in a number within {list(range(1,len(movie_list)+1))}")
                time.sleep(2)
                decide_yet = input("Have you decided which movie? (Y/N): ")
                if 'n' in decide_yet.lower():
                    leave = True
    else:
        print(f"I know you are interested in watching {user.movie.upper()}")
    
