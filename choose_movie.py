from params import movie_list
import re
def ask_which_movie(user):
    movie_pattern = "|".join(movie_list).lower()
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
