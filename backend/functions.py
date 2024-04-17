from encoding_dicts import *
import difflib
import pandas as pd
import numpy as np
from sklearn.preprocessing import (StandardScaler, MinMaxScaler, LabelEncoder)
import joblib
import shap
import xgboost as xgb
from sklearn.metrics import confusion_matrix

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


img_feats = pd.read_csv("./csv_files/img_feats.csv")
text_feats = pd.read_csv("./csv_files/text_feats.csv")
X_reference = pd.read_csv("./csv_files/X.csv")

def preprocessing(data):
    tabular_result = {}
    # Bin age
    age_bin = bin_age(data["Age"])
    
    # Whether name exists
    hasName = False
    if (data["Name"]):
        hasName = True
    
    # Treated
    treated = "Not Treated"
    if (data["Vaccinated"] and data["Dewormed"] and data["Sterilized"]):
        treated = "Treated"

    # Description Length

    # Lumped Fees
    LumpedFee = lump_fee(data["Fee"])

    breed1 = data["Breed1"]
    breed2 = data["Breed2"]

    if data["Type"] == 1:
        breed1 = find_closest_breed(breed1, dog_dict)
        breed1 = dog_dict[breed1]
        if breed2 is not None:
            breed2 = find_closest_breed(breed2, dog_dict)
            breed2 = dog_dict[breed2]
        else: 
            breed2 = 0
    else:
        breed1 = find_closest_breed(breed1, cat_dict)
        breed1 = cat_dict[breed1]
        if breed2 is not None:
            breed2 = find_closest_breed(breed2, cat_dict)
            breed2 = cat_dict[breed2]
        else: 
            breed2 = 0

    color1 = data["Colors"][0]
    color2 = 0
    color3 = 0
    if len(data["Colors"]) >= 2:
        color2 = data["Colors"][1]
    if len(data["Colors"]) == 3:
        color3 = data["Colors"][2]


    # Forming the result data row
    tabular_result["Type"] = type_encode[data["Type"]]
    tabular_result["Breed1"] = breed1
    tabular_result["Breed2"] = breed2
    tabular_result["Gender"] = gender_encode[data["Gender"]]
    tabular_result["Color1"] = colors_encode[color1]

    if color2 != 0:
        tabular_result["Color2"] = colors_encode[color2]
    else:
        tabular_result["Color2"] = color2

    if color3 != 0:
        tabular_result["Color3"] = colors_encode[color3]
    else:
        tabular_result["Color3"] = color3
    
    tabular_result["MaturitySize"] = maturity_size_encode[data["MaturitySize"]]
    tabular_result["FurLength"] = fur_length_encode[data["FurLength"]]

    if data["Vaccinated"]:
        tabular_result["Vaccinated"] = 1
    else:
        tabular_result["Vaccinated"] = 2
    
    if data["Dewormed"]:
        tabular_result["Dewormed"] = 1
    else:
        tabular_result["Dewormed"] = 2

    if data["Sterilized"]:
        tabular_result["Sterilized"] = 1
    else:
        tabular_result["Sterilized"] = 2

    # img data
    img_row = img_feats.loc[img_feats['Pet_ID'] == data["Photo"]]
    img_row = img_row.drop(columns=["Pet_ID"])

    # text data
    text_row = text_feats.loc[text_feats['PetID'] == data["Description"]]
    DescriptionLength = int(text_row['Length'])
    text_row = text_row.drop(columns=["PetID", "Length"])


    # Size Age Interaction
    scaler = StandardScaler()

    values = np.array([data["Age"], maturity_size_encode[data["MaturitySize"]]]).reshape(1, -1)
    scaled_values = scaler.fit_transform(values)

    size_age_interaction = scaled_values[0, 0] * scaled_values[0, 1]

    
    tabular_result["Health"] = health_encode[data["Health"]]
    tabular_result["State"] = states_encode[data["State"]]
    tabular_result["VideoAmt"] = data["VideoAmt"]
    tabular_result["PhotoAmt"] = data["PhotoAmt"] * 1.0
    tabular_result["AgeBinned"] = age_bin
    tabular_result["hasName"] = hasName
    tabular_result["QuantityModified"] = 1
    tabular_result["Treated"] = treated
    tabular_result["LumpedFee"] = LumpedFee
    tabular_result["DescriptionLength"] = DescriptionLength
    tabular_result["SizeAgeInteraction"] = size_age_interaction
    tabular_result["RescuerActivity"] = "Medium"

    img_dataframe = pd.DataFrame([tabular_result])

    img_dataframe = pd.concat([img_dataframe.reset_index(drop=True), img_row.reset_index(drop=True)], axis=1)

    text_dataframe = pd.concat([img_dataframe.reset_index(drop=True), text_row.reset_index(drop=True)], axis=1)

    text_dataframe = text_dataframe.drop(columns=["Unnamed: 0"])

    ohe_categorical_cols = ['Type', 'Breed1', 'Gender', 'Color1', 'Vaccinated', 'Dewormed', 'Sterilized', 'Health', 'State',
                    'AgeBinned', 'Treated']

    label_categorical_cols = ['MaturitySize', 'QuantityModified', 'LumpedFee', 'RescuerActivity']

    label_encoder = LabelEncoder()
    for col in label_categorical_cols:
        text_dataframe[col] = label_encoder.fit_transform(text_dataframe[col].astype(str))

    text_dataframe = pd.get_dummies(text_dataframe, columns=ohe_categorical_cols)

    all_columns = X_reference.columns.tolist()

    for col in all_columns:
        if col not in text_dataframe.columns:
            text_dataframe[col] = 0

    text_dataframe = text_dataframe[all_columns]

    # tabular_result = text_dataframe.squeeze().to_dict()

    model = joblib.load("./models/best_xgb_model.joblib")
    explainer = shap.TreeExplainer(model)

    text_dataframe = text_dataframe.drop(columns=["Unnamed: 0"])

    scalar = MinMaxScaler()
    text_dataframe = scalar.fit_transform(text_dataframe.values)
    shap_values = explainer.shap_values(text_dataframe)
    prediction_class = model.predict(text_dataframe)
    probabilities = model.predict_proba(text_dataframe)

    # If you want to display the most probable class and its confidence:
    max_prob_index = np.argmax(probabilities[0])  
    confidence_level = probabilities[0][max_prob_index]  

    shap_values_for_class = []

    for element in shap_values[0]:
        shap_values_for_class.append(element[prediction_class][0])
    
    abs_shap_values = np.abs(shap_values_for_class)
    top_indices = np.argsort(abs_shap_values)[-30:][::-1]
    print(top_indices)

    top_feature_names = [all_columns[i] for i in top_indices]
    top_feature_values = [shap_values_for_class[i] for i in top_indices]

    print("Top 30 features by SHAP value impact:")
    for name, value in zip(top_feature_names, top_feature_values):
        print(f"{name}: {value}")

    return tabular_result
    

def bin_age(value):
    labels = ['0-2', '2', '3-6', '6-12', '12-24', '24-60', '60+']
    ranges = [(0, 2), (2, 2), (3, 6), (6, 12), (12, 24), (24, 60), (60, float('inf'))]

    for i, (low, high) in enumerate(ranges):
        if low <= value < high:
            return labels[i]

    return 'Invalid value'

def lump_fee(value):
    categories = [0, 50, 100, 200, 150, 20, 300, 30, 250, 1]
    
    if value > 300:
        return 'Other'
    
    closest_value = min(categories, key=lambda x: (abs(x - value), x))
    
    return closest_value

def find_closest_breed(breed, breed_dict):
    breed_list = list(breed_dict.keys())
    closest_match = difflib.get_close_matches(breed, breed_list, n=1, cutoff=0)
    if closest_match:
        return closest_match[0]
    else:
        return None