from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from functions import preprocessing
from sklearn.metrics import confusion_matrix
import numpy as np

def quadratic_kappa(actuals, preds, N=4):
    """This function calculates the Quadratic Kappa Metric used for Evaluation in the PetFinder competition
    at Kaggle. It returns the Quadratic Weighted Kappa metric score between the actual and the predicted values
    of adoption rating."""
    w = np.zeros((N,N))
    O = confusion_matrix(actuals, preds)
    for i in range(len(w)):
        for j in range(len(w)):
            w[i][j] = float(((i-j)**2)/(N-1)**2)

    act_hist=np.zeros([N])
    for item in actuals:
        act_hist[item]+=1

    pred_hist=np.zeros([N])
    for item in preds:
        pred_hist[item]+=1

    E = np.outer(act_hist, pred_hist);
    E = E/E.sum();
    O = O/O.sum();

    num=0
    den=0
    for i in range(len(w)):
        for j in range(len(w)):
            num+=w[i][j]*O[i][j]
            den+=w[i][j]*E[i][j]
    return (1 - (num/den))

def quadratic_kappa_eval(preds, dtrain):
    labels = dtrain.get_label()  # Extract the true labels
    preds = np.argmax(preds, axis=1)  # Convert probabilities to predicted class labels
    return 'qkappa', -quadratic_kappa(labels, preds, N=4)  # Return a tuple (name, value)


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

sample_json = {
    "Name": "Nibble",
    "Type": "Dog",
    "Age": 3,
    "Gender": "Male",
    "Breed1": "Golden",
    "Breed2": None,
    "Colors": ["Brown", "White"],
    "MaturitySize": "Medium",
    "FurLength": "Long",
    "Vaccinated": True,
    "Dewormed": False,
    "Sterilized": False,
    "Health": "Healthy",
    "Fee": 0,
    "State": "Selangor",
    "PhotoAmt": 1,
    "VideoAmt": 1,
    "Description": "002efc654", #number chosen
    "Photo": "002efc654" #number chosen
}

sample_result = {
    "Result": "1 Week",
    "Confidence": 0.8,
    "Shapleys": {"FurLength": 0.221, "PhotoAmt": 0.11},
    "Recommendations": ['Increase photo amount', 'Add more description', 'Don`t vaccinate'],
},

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask app!"})

@app.post('/upload')
@cross_origin(options=None)
def upload():
    if request.method == "POST":
        data = request.json
        # data = sample_json
    preprocessed_data = preprocessing(data)
    return jsonify(sample_result)

@app.post('/test')
def test():
    return jsonify({"message": "testing"})

if __name__ == "__main__":
    app.run(debug=True)
