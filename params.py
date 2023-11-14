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

response_for_intent ={
    "default":["Sorry, I can't understand you. Can you give more details","Please give me more details.","Can you say it again with specific keywords"],
    "greet":["Nice to meet you! What can I help you?","Hi, are you alright?","Hello, good to see you again!"],
    "thankyou":["You're Welcome! What else can I help you?","No worries, glad to help you here"]
}