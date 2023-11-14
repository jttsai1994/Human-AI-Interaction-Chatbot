import re
import random

import params

patterns = params.patterns
responses = params.response_for_intent
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message 
        if re.search(pattern,message):
            matched_intent = intent
    return matched_intent

def respond(message):
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = "default"
    if intent in responses:
        key = intent
    response = random.choice(responses[key])
    return response