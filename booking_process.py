import re
from params import responses_movie_list
import params
import choose_movie
import choose_movie_time
import choose_paymethod
import time
import confirm_movie_detail
def booking(user):
    movie_pattern = "|".join(params.movie_list).lower()
    stop = False
    while not all([user.movie,user.visitDate,user.visitTime]):
    # while not all([user.movie,user.visitDate,user.visitTime,user.payMethod]):
        choose_movie.ask_which_movie(user)
        if user.movie: #only ask for date, time and pay method if the movie is decided
            choose_movie_time.decide_date(user)
            choose_movie_time.decide_Time(user)
            if not user.confirm:
                confirm_movie_detail.ask_to_confirm(user)
            choose_paymethod.ask_payment_method(user)
        
        
        # response = match_rules.send_message(user_input)
        