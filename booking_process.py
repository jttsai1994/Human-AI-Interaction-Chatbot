import re
import params
import choose_movie
import choose_movie_time
def booking(user):
    movie_pattern = "|".join(params.movie_list).lower()
    stop = False
    while not all([user.movie,user.visitDate]):
    # while not all([user.movie,user.visitDate,user.visitTime,user.payMethod]):
        choose_movie.ask_which_movie(user)
        choose_movie_time.decide_date(user)
        if not user.visitTime:
            pass

        elif not user.payMethod:
            pass

        elif not user.confirm:
            pass
        
        
        # response = match_rules.send_message(user_input)
        