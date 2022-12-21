import joblib
from sklearn.svm import SVC

def model(review_text):
    clf = joblib.load('svc_model.pkl') 

    review = []
    #print(review_text)
    review.append(review_text)
    val = clf.predict(review)
   
    return val
