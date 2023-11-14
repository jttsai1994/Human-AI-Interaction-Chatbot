from joblib import load
count_vect = load('count_vect.joblib')
tfidf_transformer = load('tfidf_transformer.joblib')
clf = load('classifier.joblib')
import csv

qn_q={}
q_a = {}
with open("./QA.csv", 'r',encoding='utf-8') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        #store QuestionNumber-Question, Question-Answer
        qn_q[row[0]] = row[1]
        if row[1] in q_a:
            q_a[row[1]].append(row[2])
        else:
            q_a[row[1]]=[row[2]]
        

def answer(msg):
    new_data = [msg]
    processed_newdata = count_vect.transform(new_data) 
    processed_newdata = tfidf_transformer.transform(processed_newdata)
    predict_question_number = clf.predict(processed_newdata)
    answer = None
    if predict_question_number:
        answer  = q_a[qn_q[predict_question_number]]
    print(answer)