import re
import params
def decide_date(user):
    movie_index = params.movie[user.movie]
    movie_date = params.display_date[movie_index]
    days_mapping = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    days_list = [days_mapping[index] for index in movie_date]
    days_pattern = '|'.join(list(days_mapping.values())).lower()
    if not user.visitDate:
        print(f"Seems like you haven't choose the Date to watch {user.moive}")
        user_ans= input(f" We can watch {user.movie} on:{days_list}, which day would you like?")
        if re.search(days_pattern,user_ans.lower()):
            user_date = re.search(days_pattern,user_ans.lower())[0]
            user.visit_at(user_date)
            print(f"OK, looking forward to see you on{user_date}")
        else:
            print(f"Sorry, we can't arrange with your answer.")
    else:
        pass




def decide_Time(user):
    pass