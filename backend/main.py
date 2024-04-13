from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from functions import preprocessing

app = Flask(__name__)
CORS(app)

sample_json = {
    "Name": "Nibble",
    "Type": "Dog",
    "Age": 3,
    "Gender": "Male",
    "Breed1": "Golden",
    "Breed2": None,
    "Colors": ["Blue", "Green"],
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
    "Description": "3aa", #number chosen
    "Photo": "2aa" #number chosen
}

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
    return jsonify(preprocessed_data)

@app.post('/test')
def test():
    return jsonify({"message": "testing"})

if __name__ == "__main__":
    app.run(debug=True)
