def preprocessing(data):
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