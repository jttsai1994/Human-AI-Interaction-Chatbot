from joblib import load
count_vect = load('count_vect.joblib')
tfidf_transformer = load('tfidf_transformer.joblib')
clf = load('classifier.joblib')

from sklearn.metrics.pairwise import cosine_similarity


def answer(msg):
    new_data = [msg]
    processed_newdata = count_vect.transform(new_data) 
    processed_newdata = tfidf_transformer.transform(processed_newdata)
    possible_intent = clf.predict(processed_newdata)[0] #it return a result in list, I want to retrieve string

    # answer = None
    # if predict_question_number:
    #     answer  = random.choice(q_a[qn_q[predict_question_number]])
    return possible_intent