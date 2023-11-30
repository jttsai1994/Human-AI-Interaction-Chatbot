import csv
# import os
# from sklearn.model_selection import train_test_split
# from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer 
from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score , f1_score , confusion_matrix
from joblib import dump
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
qn_q={}
q_a = {}
questions = []
intents =[] 
with open("./movie_intent_qa.csv", 'r',encoding='utf-8') as file:
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
dump(q_a,'QA_Dictionary')
dump(qn_q,'Qid_Q_dict')
from nltk.stem.snowball import PorterStemmer
p_stemmer = PorterStemmer()
analyzer = CountVectorizer().build_analyzer()
def stemmed_words(doc):
    return (p_stemmer.stem(w) for w in analyzer(doc))

stem_vectorizer = CountVectorizer(analyzer=stemmed_words)    
train_counts = stem_vectorizer.fit_transform(questions)

tfidf_transformer = TfidfTransformer(use_idf=True, sublinear_tf=True).fit(train_counts)
train_tf = tfidf_transformer.transform(train_counts)

clf = LogisticRegression(random_state=0).fit(train_tf, intents)

# dump(stem_vectorizer , 'count_vect.joblib')
# dump(tfidf_transformer , 'tfidf_transformer.joblib')
# dump(train_tf , 'pretrainMatrix.joblib')

dump(clf , 'classifier.joblib')
def answer(msg):
    new_data = [msg]
    processed_newdata = stem_vectorizer.transform(new_data) 
    processed_newdata = tfidf_transformer.transform(processed_newdata)
    scores = [cosine_similarity(processed_newdata, _q) for _q in train_tf]
    possible_intent = intents[np.argmax(scores)]

    possible_intent = "defualt"

    if scores[np.argmax(scores)] > 0.8: #add a threhold of cos_similarity
        possible_intent = intents[np.argmax(scores)]

    return possible_intent

def answer_clf(msg):
    new_data = [msg]
    processed_newdata = stem_vectorizer.transform(new_data) 
    processed_newdata = tfidf_transformer.transform(processed_newdata)
    possible_intent = clf.predict(processed_newdata)[0] #it return a result in list, I want to retrieve string

    # answer = None
    # if predict_question_number:
    #     answer  = random.choice(q_a[qn_q[predict_question_number]])
    return possible_intent
