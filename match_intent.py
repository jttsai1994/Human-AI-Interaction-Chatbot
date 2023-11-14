from joblib import load
import csv
import numpy as np
intent_questions = []
intents =[] 
with open("./Intent.csv", 'r',encoding='utf-8') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        intents.append(row[0])        
        intent_questions.append(row[1])

def match_intent(msg):
    vectorizer = load('intent_TfidfVectorizer.joblib')
    intent_question_array = load('intent_question_array.joblib')
    new_data = [msg]
    _v = vectorizer.transform(new_data)
    new_arr = _v.toarray()

    scores = [np.dot(new_arr, _q) for _q in intent_question_array]
    
    #return the most possible intent by cos_similarity
    possible_intent = "defualt"

    if scores[np.argmax(scores)] > 0.8: #add a threhold of cos_similarity
        possible_intent = intents[np.argmax(scores)]

    return possible_intent
    