from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

sample_json = {
    "Name": "Nibble",
    "Type": "Dog",
    "Age": 3,
    "Gender": "Male",
    "Breed1": "Golden",
    "Breed2": None,
    "Color1": "Blue",
    "Color2": "Green",
    "Color3": None,
    "MaturitySize": "Medium",
    "FurLength": "Long",
    "Vaccinated": True,
    "Dewormed": False,
    "Sterilized": False,
    "Health": "Healthy",
    "Fee": 0,
    "State": "Selangor",
    "Description": 3, #number chosen
    "Photo": 2 #number chosen
}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask app!"})

@app.route('/upload', methods=["GET", "POST"])
@cross_origin(options=None)
def upload():
    if request.method == "POST":
        # data = request.form
        data = sample_json
        

if __name__ == "__main__":
    app.run(debug=True)
