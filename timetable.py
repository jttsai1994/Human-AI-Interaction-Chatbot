from params import movie_list
import re
import random
from params import responses_movie_list
import params
def which_timetable(user):
    days_mapping = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    print(random.choice(responses_movie_list))
    user_ans= input(f"Which movie are you interested in? (within {list(range(1,len(movie_list)+1))}) :")
    if int(user_ans) in list(range(1,len(movie_list)+1)):
        interested_movie_index = int(user_ans)-1
        perform_date = [days_mapping[index] for index in params.display_date[interested_movie_index]]
        perform_time = params.display_time[interested_movie_index]
        print(f"""
OK, the movie {movie_list[interested_movie_index].upper()} will be played on {perform_date}
The time is shown as follows {perform_time}. """)
    else:
        print(f"Sorry, we can't arrange with your answer.")
    if user.movie:
        interested_movie_index = params.movie[user.movie]
        perform_date = [days_mapping[index] for index in params.display_date[interested_movie_index]]
        perform_time = params.display_time[interested_movie_index]
        print(f"You booked for the movie {user.movie.upper()}")
        print(f"{user.movie.upper()} will be played on {perform_date}, and the time is shown as follows {perform_time} ")
