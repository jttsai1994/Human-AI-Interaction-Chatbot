import re
# rules for matching sentences
rules = {
'hello|hi':["Nice to meet you! What can I help you?","Hi, are you alright?","Hello, good to see you again!"],
'I want (.*)': 
                ['What would it mean if you got {0}',
                'Why do you want {0}',
                "What's stopping you from getting {0}"],
 'do you remember (.*)':
                        ['Did you think I would forget {0}',
                        "Why haven't you been able to forget {0}",
                        'What about {0}',
                        'Yes .. and?'],
 'do you think (.*)': 
                    ['if {0}? Absolutely.', 'No chance'],
 'if (.*)': 
                ["Do you really think it's likely that {0}",
                'Do you wish that {0}',
                'What do you think about {0}',
                'Really--if {0}']
  }
# keywords for storing intent:keywords
keywords = {
    'goodbye': ['bye', 'farewell'],
    'greet': ['hello', 'hi', 'hey'],
    'thankyou': ['thank', 'thx']}


# convert keywords into reg pattern for each intent
patterns = {}

for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))

responses_usual ={
    # "default":["default"],
    "default":["Sorry, I can't understand you. Can you give more details","Please give me more details.","Can you say it again with specific keywords"],
    "greet":["Nice to meet you! Would you like to watch a movie?","Hi, let me help you to find a movie and enjoy in our cinema.","Hello, good to see you again! How about watching a movie?"],
    "thankyou":["You're Welcome! What else can I help you?","No worries, glad to help you here"],
    "discoverability":["I am a chatbot to help you book a ticket to the movie","I 'm here to help you get the ticket to the movie.","I can answer some simple question about how to book a movie ticket."]
}
# movie info
movie_list = ['Spider Man','Joker','Oppenhimer','Misson Impossible']
movie={
'spider man':0,
'joker': 1,
'oppenhimer':2,
'misson impossible':3
}
responses_movie_list=[
    f'Our current lineup features popular titles such as {movie_list}',
    f'The cinema is currently showcasing a diverse selection of films, including {movie_list}',
    f'"Of course! We have an exciting roster of films for you, including {movie_list}'
    ]

display_date={
    0:[1,3,5,6],
    1:[2,3,4,7],
    2:[1,2,3,4,5,6,7],
    3:[5,6,7]
}
display_time={
    0:['09:00','14:00','18:00'],
    1:['12:00','16:00','19:00'],
    2:['11:30','13:30','16:00','17:30','20:00','21:00'],
    3:['11:00','14:00','16:00','18:00']
}

display_room={
    0:['room1','room2','room1'],
    1:['room3','room3','room4'],
    2:['room5','room5','room5','room5','room5','room5'],
    3:['room2','room3','room2','room3']
}

