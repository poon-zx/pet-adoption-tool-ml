from encoding_dicts import *
import difflib
import pandas as pd
import numpy as np
from sklearn.preprocessing import (StandardScaler, MinMaxScaler, LabelEncoder)
import joblib
import shap
import xgboost as xgb
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from metrics import quadratic_kappa, quadratic_kappa_eval

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
    tabular_result["RescuerActivity"] = "High"

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

    model = joblib.load("./models/best_xgb_model.joblib")
    explainer = shap.TreeExplainer(model)

    text_dataframe = text_dataframe.drop(columns=["Unnamed: 0"])

    scalar = joblib.load("./models/MinMaxscaler.save") 
    text_dataframe_scale = scalar.transform(text_dataframe.values)
    shap_values = explainer.shap_values(text_dataframe_scale)
    prediction_class = model.predict(text_dataframe_scale)
    probabilities = model.predict_proba(text_dataframe_scale)

    # If you want to display the most probable class and its confidence:
    max_prob_index = np.argmax(probabilities[0])  
    confidence_level = float(probabilities[0][max_prob_index])

    shap_values_for_class = []
    shap_values_for_chart = []

    for element in shap_values[0]:
        shap_values_for_class.append(element[0])
        shap_values_for_chart.append(element[prediction_class[0]])
    
    abs_shap_values = np.abs(shap_values_for_class)
    top_indices_class = np.argsort(abs_shap_values)[-80:][::-1]

    abs_shap_values_chart = np.abs(shap_values_for_chart)
    top_indices_chart = np.argsort(abs_shap_values_chart)[-80:][::-1]

    top_feature_names= [all_columns[i] for i in top_indices_class]
    top_feature_values = [shap_values_for_class[i] for i in top_indices_class]

    top_feature_names_chart = [all_columns[i] for i in top_indices_chart]
    top_feature_values_chart = [shap_values_for_chart[i] for i in top_indices_chart]


    counter = 0
    id = 0
    suggestion_result = []
    shapleys = {}
    reference = {}
    if prediction_class == 0:
        reference = good_recommendations
    else:
        reference = bad_recommendations

    if prediction_class == 0:
        for feat in top_feature_names:
            if feat in reference and top_feature_values[id] > 0:
                suggestion = get_good_suggestion(reference, feat, int(text_dataframe[feat]))
                if suggestion is not None:
                    counter += 1
                    suggestion_result.append(suggestion)
                    shapleys[feat] = float(top_feature_values[id])
            id += 1
            if counter == 5:
                break
    else:
        for feat in top_feature_names:
            if feat in reference and top_feature_values[id] < 0:
                suggestion = get_bad_suggestion(reference, feat, int(text_dataframe[feat]))
                if suggestion is not None:
                    counter += 1
                    suggestion_result.append(suggestion)
                    shapleys[feat] = float(top_feature_values[id])
            id += 1
            if counter == 5:
                break

    final_result = {
        "Result": adoption_speed_mapping[int(prediction_class)],
        "Confidence": confidence_level,
        "Shapleys": shapleys,
        "Recommendations": suggestion_result     
    }

    # plot_shap_waterfall(top_feature_values, top_feature_names)
    shap_values = top_feature_values_chart
    feature_names = top_feature_names_chart

    top_n = min(20, len(shap_values) // 2)
    sorted_indices = sorted(range(len(shap_values)), key=lambda i: shap_values[i])
    top_negative_indices = sorted_indices[:top_n]
    top_positive_indices = sorted_indices[-top_n:]

    top_indices = top_negative_indices + top_positive_indices

    selected_shap_values = [float(shap_values[i]) for i in top_indices]
    selected_feature_names = [feature_names[i] for i in top_indices]

    print(final_result)
    return [final_result, selected_shap_values, selected_feature_names]

   

def plot_shap_waterfall(shap_values, feature_names, top_n=20):
    top_n = min(top_n, len(shap_values) // 2)

    sorted_indices = sorted(range(len(shap_values)), key=lambda i: shap_values[i])
    top_negative_indices = sorted_indices[:top_n]
    top_positive_indices = sorted_indices[-top_n:]

    top_indices = top_negative_indices + top_positive_indices

    selected_shap_values = [shap_values[i] for i in top_indices]
    selected_feature_names = [feature_names[i] for i in top_indices]

    plt.figure(figsize=(10, 8))
    plt.barh(range(len(selected_shap_values)), selected_shap_values, color=['r' if val < 0 else 'b' for val in selected_shap_values])
    plt.yticks(range(len(selected_shap_values)), selected_feature_names)
    plt.xlabel("SHAP Value (Impact on Model Output)")
    plt.title(f"Top {top_n} Positive and Top {top_n} Negative SHAP Values")
    plt.gca().invert_yaxis()  
    plt.tight_layout()
    plt.savefig('top_shap_values.png')
    plt.close()


def get_bad_suggestion(ref, category, value):
    conditions = ref.get(category, {})
    
    if category == "VideoAmt":
        key = 0 if value == 0 else 1
    elif category in ["PhotoAmt", "DescriptionLength", "reading_time"]:
        key = 0 if value <= 3 else 1
    elif category == "LumpedFee":
        key = 0 if value == 0 else 1
    elif category == "QuantityModified":
        key = 1 if value > 1 else None
    elif category == "Blurriness":
        key = 0 if value < 60 else None
    elif category == "polarity":
        key = 0 if value < 0.25 else 1
    elif category == "reading_ease":
        key = 0 if value < 80 else None
    elif category in ["Vaccinated_2", "Dewormed_2", "Sterilized_2", "FurLength"]:
        key = value  
    else:
        key = None

    return conditions.get(key, None)

def get_good_suggestion(ref, category, value):
    if category == "VideoAmt":
        key = 1 if value > 0 else 0  
    elif category == "PhotoAmt":
        key = 0 if value <= 3 else 1
    elif category == "QuantityModified":
        key = 0 if value <= 1 else 1
    elif category == "LumpedFee":
        key = 0 if value == 0 else 1
    elif category == "DescriptionLength":
        key = 0 if value < 70 else 1
    elif category == "Blurriness":
        key = 1 if value > 60 else 0  
    elif category == "polarity":
        key = 0 if value < 0.25 else 1
    elif category == "reading_ease":
        key = 0 if value < 80 else None
    elif category in ["Vaccinated_1", "Dewormed_1", "Sterilized_1", "FurLength"]:
        key = value  
    else:
        key = None  

    # Fetch the conditions and messages for the given category
    recommendations = ref.get(category, {})
    
    # Return the message if the key exists in the recommendations, otherwise return None
    return recommendations.get(key, None)

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