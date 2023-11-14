import csv
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer 

from sklearn.feature_extraction.text import TfidfVectorizer

import numpy as np
from joblib import dump

intent_questions = []
intents =[] 
with open("./Intent.csv", 'r',encoding='utf-8') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        intents.append(row[0])        
        intent_questions.append(row[1])
        
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(intent_questions)
intent_question_array = X.toarray()

# save vectorizer and intent_question_array as joblib file, load in match_intent.py
dump(vectorizer , 'intent_TfidfVectorizer.joblib')
dump(intent_question_array,'intent_question_array.joblib')