import re

import params
patterns = params.patterns
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message 
        if re.search(pattern,message):
            matched_intent = intent
    return matched_intent