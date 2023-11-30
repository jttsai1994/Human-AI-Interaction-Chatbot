import re
import params
def decide_date(user):
    movie_index = params.movie[user.movie]
    movie_date = params.display_date[movie_index]
    days_mapping = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    days_list = [days_mapping[index] for index in movie_date]
    days_pattern = '|'.join(list(days_mapping.values())).lower()
    if not user.visitDate:
        print(f"Seems like you haven't choose the Date to watch {user.movie}")
        user_ans= input(f" We can watch {user.movie} on:{days_list}, which day would you like?: ")
        if re.search(days_pattern,user_ans.lower()):
            user_date = re.search(days_pattern,user_ans.lower())[0]
            user.visit_at(user_date.upper())
            print(f"OK, looking forward to see you on {user.visitDate}")
        else:
            print(f"Sorry, we can't arrange with your answer.")
    else:
        pass




def decide_Time(user):
    movie_index = params.movie[user.movie]
    movie_time = params.display_time[movie_index]
    while not user.visitTime:
        if not user.visitTime:
            print(f"Seems like you haven't choose the Time to watch {user.movie} on {user.visitDate}")
            user_ans= input(f"""
You can choose one from the following timetable for {user.movie} --- {movie_time}: 
please type in the index of time that you select. (within {list(range(1,len(movie_time)+1))})
                                                """)
            if int(user_ans) in list(range(1,len(movie_time)+1)):
                user.visit_time(movie_time[int(user_ans)])
                print(f"OK, looking forward to see you on {user.visitTime}")
            else:
                print(f"Sorry, we can't arrange with your answer.")
        else:
            pass