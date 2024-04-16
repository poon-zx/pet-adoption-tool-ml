from encoding_dicts import *
import difflib
import pandas as pd
import numpy as np
from sklearn.preprocessing import (StandardScaler, MinMaxScaler, LabelEncoder)
import joblib
import shap
import xgboost

img_feats = pd.read_csv("./csv_files/img_feats.csv")
text_feats = pd.read_csv("./csv_files/text_feats.csv")

def preprocessing(data):
    tabular_result = {}
    # Bin age
    age_bin = bin_age(data["Age"])
    
    # Whether name exists
    hasName = False
    if (data["Name"]):
        hasName = True
    
    # Treated
    treated = False
    if (data["Vaccinated"] and data["Dewormed"] and data["Sterilized"]):
        treated = True

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
        breed1 = find_closest_breed(breed1, cat_dict)
        breed1 = cat_dict[breed1]
        if breed2 is not None:
            breed2 = find_closest_breed(breed2, cat_dict)
            breed2 = cat_dict[breed2]

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
    DescriptionLength = text_row['Length'].item()
    text_row = text_row.drop(columns=["PetID", "Length"])


    # Size Age Interaction
    scaler = StandardScaler()

    values = np.array([data["Age"], maturity_size_encode[data["MaturitySize"]]]).reshape(1, -1)
    print("VALUES")
    print(values)
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
    
    # tabular_result = text_dataframe.squeeze().to_dict()

    model = joblib.load("best_xgb_model.joblib")
    explainer = shap.TreeExplainer(model)
    print("pd dataframe")
    print(text_dataframe["AgeBinned"])
    print(text_dataframe["RescuerActivity"])
    print(text_dataframe)

    label_encoder = LabelEncoder()
    text_dataframe['Breed2'] = label_encoder.fit_transform(text_dataframe['Breed2'])
    text_dataframe['AgeBinned'] = label_encoder.fit_transform(text_dataframe['AgeBinned'])
    text_dataframe['RescuerActivity'] = label_encoder.fit_transform(text_dataframe['RescuerActivity'])

    print(text_dataframe.dtypes)


    shap_values = explainer.shap_values(text_dataframe)
    print(shap_values)
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