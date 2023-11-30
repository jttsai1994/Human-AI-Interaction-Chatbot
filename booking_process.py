import re
import params
import choose_movie
import choose_movie_time
def booking(user):
    movie_pattern = "|".join(params.movie_list).lower()
    stop = False
    while not stop:
        choose_movie.ask_which_movie(user)
        choose_movie_time.decide_date(user)
        if not user.visitTime:
            pass

        elif not user.payMethod:
            pass

        elif not user.confirm:
            pass
        
        


        user_input = input(" (enter 'stop' to quit,or press enter to continue): ")
        if user_input.lower() == 'stop':
            print("Goodbye!")
            stop = True
        # response = match_rules.send_message(user_input)
        