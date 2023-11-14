import csv
import os
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , f1_score , confusion_matrix
import nltk
nltk.download('stopwords')
qn_q={}
q_a = {}
questions = []
question_numbers =[] 
with open("./QA.csv", 'r',encoding='utf-8') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        #store QuestionNumber-Question, Question-Answer
        qn_q[row[0]] = row[1]
        if row[1] in q_a:
            q_a[row[1]].append(row[2])
        else:
            q_a[row[1]]=[row[2]]
        
        questions.append(row[1])
        question_numbers.append(row[0])

count_vect = CountVectorizer(stop_words=stopwords.words('english'))    
train_counts = count_vect.fit_transform(questions)

tfidf_transformer = TfidfTransformer(use_idf=True, sublinear_tf=True).fit(train_counts)
train_tf = tfidf_transformer.transform(train_counts)

clf = LogisticRegression(random_state=0).fit(train_tf, question_numbers)

import pickle
with open("QA_Model.pickle", "wb") as f:
    pickle.dump(clf , f)

