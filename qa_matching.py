from joblib import load
count_vect = load('count_vect.joblib')
tfidf_transformer = load('tfidf_transformer.joblib')
clf = load('classifier.joblib')
import csv
import random
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


qn_q={}
q_a = {}
questions = []
intents =[] 
with open("./QA＿intent.csv", 'r',encoding='utf-8') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        #store QuestionNumber-Question, Question-Answer
        qn_q[row[0]] = row[1]
        if row[1] in q_a:
            q_a[row[1]].append(row[2])
        else:
            q_a[row[1]]=[row[2]]
        
        questions.append(row[1])
        intents.append(row[0])
        

def answer(msg):
    new_data = [msg]
    processed_newdata = count_vect.transform(new_data) 
    processed_newdata = tfidf_transformer.transform(processed_newdata)
    possible_intent = clf.predict(processed_newdata)[0] #it return a result in list, I want to retrieve string

    # answer = None
    # if predict_question_number:
    #     answer  = random.choice(q_a[qn_q[predict_question_number]])
    return possible_intent