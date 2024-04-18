adoption_speed_mapping = {
    0: 'Adopted between 0 and 7 days',
    1: 'Adopted between 8 and 30 days',
    2: 'Adopted between 31 and 90 days',
    3: 'No adoption after 100 days'
}

bad_recommendations = {
    "FurLength": {
        1: "Consider growing out your pet's hair to a longer length",
        3: "Keeping your pet's hair shorter might improve adoption rates"
    }, 
    "VideoAmt": { # if 0, then 0, if more than 0, then 1
        0: "Upload more videos!",
    },
    "PhotoAmt": { # if 3 or less, then 0, if 4 or more, then 1
        0: "Your listing should contain more photos of your pet",
        1: "Consider having less pictures as it may appear too cluttered"
    },
    "QuantityModified": { # if more than 1, then 1
        1: "You should have separate listings for each pet to improve adoption speeds"
    },
    "LumpedFee": { # if 0, then 0, else 1
        0: "Slightly increasing the adoption fee might attract more adopters",
        1: "Reducing the cost of adoption or making it free might attract potential adopters"
    }, 
    "DescriptionLength": { # if below 70 words, then 0, else 1
        0: "Increasing the length of your description could give potential adopters more information about your pet",
        1: "Decrease the length of your description, keep it short and sweet!"
    },
    "Blurriness": { # if below 60, then 0, else 1
        0: "Choose a less blurry image for your adoption listing!"
    },
    "polarity": { # if below 0.25 then 0, else 1
        0: "Your description can be more positive! That would attract more potential adopters"
    },
    "reading_time": { # if below 4 then 0, else 1
        0: "Your description's estimated reading time might be too short, consider making it longer!",
        1: "Your description's estimated reading time is too long, do make it shorter"
    },
    "reading_ease": { # if below 80 then 0, else 1
        0: "Your description is not readable enough, do increase its readability by making sentences shorter or less complicated words!"
    }, 
    "Vaccinated_2": {
        1: "Do vaccinate your pet, this would likely increase the number of potential adopters!"
    },
    "Dewormed_2": {
        1: "Do deworm your pet, this would likely increase the number of potential adopters!"
    },
    "Sterilized_2": {
        1: "Do sterilize your pet, this would likely increase the number of potential adopters!"
    }    
}

good_recommendations = {
    "FurLength": {
        1: "Continue keeping your pet's hair short, that is popular with adopters!",
        3: "Continue keeping your pet's hair long, that is popular with adopters!"
    }, 
    "VideoAmt": { # if 0, then 0, if more than 0, then 1
        1: "It is good that you uploaded many videos!",
    },
    "PhotoAmt": { # if 3 or less, then 0, if 4 or more, then 1
        0: "It is good that you have minimal photos of your pet, that is helping with adopters",
        1: "It is good that you have many photos of your pet, adopters can have a good idea of how cute your pet is!"
    },
    "QuantityModified": { # if more than 1, then 1
        0: "Good that the listing only contains one pet, making it easier to attract potential adopters!"
    },
    "LumpedFee": { # if 0, then 0, else 1
        0: "Keeping the adoption fee free has helped in attracting potential adopters",
        1: "It is good that you charged a small fee for the adoption of your pet"
    }, 
    "DescriptionLength": { # if below 70 words, then 0, else 1
        0: "You kept your listing description short and sweet, nice!",
        1: "Your informative description has helped potential adopters learn more about your pet!"
    },
    "Blurriness": { # if below 60, then 0, else 1
        1: "It is good that you chose a listing picture that is not blurry!"
    },
    "polarity": { # if below 0.25 then 0, else 1
        1: "The high polarity and positivity of your description has helped in attracting adopters"
    },
    "reading_time": { # if below 4 then 0, else 1
        0: "Your description is short and has a low reading time, catching the eye of potential adopters!",
        1: "The reading time of your description is slightly longer, providing sufficient information to adopters"
    },
    "reading_ease": { # if below 80 then 0, else 1
        1: "Your description has high readability, which definitely has helped in increasing the popularity of your listing"
    }, 
    "Vaccinated_1": {
        1: "The fact that you vaccinated your pet has played a part in attracting more potential adopters!"
    },
    "Dewormed_1": {
        1: "The fact that you dewormed your pet has played a part in attracting more potential adopters!"
    },
    "Sterilized_1": {
        1: "The fact that you sterilized your pet has played a part in attracting more potential adopters!"
    }    
}

type_encode = {
    "Dog": 1,
    "Cat": 2
}

gender_encode = {
    "Male": 1,
    "Female": 2
}

maturity_size_encode = {
    "Small": 1,
    "Medium": 2, 
    "Large": 3,
    "Extra Large": 4
}

fur_length_encode = {
    "Short": 1,
    "Medium": 2,
    "Long": 3
}

health_encode = {
    "Healthy": 1,
    "Minor Injury": 2,
    "Serious Injury": 3
}

colors_encode = {
    'Black': 1,
    'Brown': 2,
    'Golden': 3,
    'Yellow': 4,
    'Cream': 5,
    'Gray': 6,
    'White': 7
}

states_encode = {
    'Johor': 41336,
    'Kedah': 41325,
    'Kelantan': 41367,
    'Kuala Lumpur': 41401,
    'Labuan': 41415,
    'Melaka': 41324,
    'Negeri Sembilan': 41332,
    'Pahang': 41335,
    'Perak': 41330,
    'Perlis': 41380,
    'Pulau Pinang': 41327,
    'Sabah': 41345,
    'Sarawak': 41342,
    'Selangor': 41326,
    'Terengganu': 41361
}

dog_dict = {
    'Affenpinscher': 1,
    'Afghan Hound': 2,
    'Airedale Terrier': 3,
    'Akbash': 4,
    'Akita': 5,
    'Alaskan Malamute': 6,
    'American Bulldog': 7,
    'American Eskimo Dog': 8,
    'American Hairless Terrier': 9,
    'American Staffordshire Terrier': 10,
    'American Water Spaniel': 11,
    'Anatolian Shepherd': 12,
    'Appenzell Mountain Dog': 13,
    'Australian Cattle Dog/Blue Heeler': 14,
    'Australian Kelpie': 15,
    'Australian Shepherd': 16,
    'Australian Terrier': 17,
    'Basenji': 18,
    'Basset Hound': 19,
    'Beagle': 20,
    'Bearded Collie': 21,
    'Beauceron': 22,
    'Bedlington Terrier': 23,
    'Belgian Shepherd Dog Sheepdog': 24,
    'Belgian Shepherd Laekenois': 25,
    'Belgian Shepherd Malinois': 26,
    'Belgian Shepherd Tervuren': 27,
    'Bernese Mountain Dog': 28,
    'Bichon Frise': 29,
    'Black and Tan Coonhound': 30,
    'Black Labrador Retriever': 31,
    'Black Mouth Cur': 32,
    'Black Russian Terrier': 33,
    'Bloodhound': 34,
    'Blue Lacy': 35,
    'Bluetick Coonhound': 36,
    'Boerboel': 37,
    'Bolognese': 38,
    'Border Collie': 39,
    'Border Terrier': 40,
    'Borzoi': 41,
    'Boston Terrier': 42,
    'Bouvier des Flanders': 43,
    'Boxer': 44,
    'Boykin Spaniel': 45,
    'Briard': 46,
    'Brittany Spaniel': 47,
    'Brussels Griffon': 48,
    'Bull Terrier': 49,
    'Bullmastiff': 50,
    'Cairn Terrier': 51,
    'Canaan Dog': 52,
    'Cane Corso Mastiff': 53,
    'Carolina Dog': 54,
    'Catahoula Leopard Dog': 55,
    'Cattle Dog': 56,
    'Caucasian Sheepdog (Caucasian Ovtcharka)': 57,
    'Cavalier King Charles Spaniel': 58,
    'Chesapeake Bay Retriever': 59,
    'Chihuahua': 60,
    'Chinese Crested Dog': 61,
    'Chinese Foo Dog': 62,
    'Chinook': 63,
    'Chocolate Labrador Retriever': 64,
    'Chow Chow': 65,
    'Cirneco dell\'Etna': 66,
    'Clumber Spaniel': 67,
    'Cockapoo': 68,
    'Cocker Spaniel': 69,
    'Collie': 70,
    'Coonhound': 71,
    'Corgi': 72,
    'Coton de Tulear': 73,
    'Curly-Coated Retriever': 74,
    'Dachshund': 75,
    'Dalmatian': 76,
    'Dandi Dinmont Terrier': 77,
    'Doberman Pinscher': 78,
    'Dogo Argentino': 79,
    'Dogue de Bordeaux': 80,
    'Dutch Shepherd': 81,
    'English Bulldog': 82,
    'English Cocker Spaniel': 83,
    'English Coonhound': 84,
    'English Pointer': 85,
    'English Setter': 86,
    'English Shepherd': 87,
    'English Springer Spaniel': 88,
    'English Toy Spaniel': 89,
    'Entlebucher': 90,
    'Eskimo Dog': 91,
    'Feist': 92,
    'Field Spaniel': 93,
    'Fila Brasileiro': 94,
    'Finnish Lapphund': 95,
    'Finnish Spitz': 96,
    'Flat-coated Retriever': 97,
    'Fox Terrier': 98,
    'Foxhound': 99,
    'French Bulldog': 100,
    'Galgo Spanish Greyhound': 101,
    'German Pinscher': 102,
    'German Shepherd Dog': 103,
    'German Shorthaired Pointer': 104,
    'German Spitz': 105,
    'German Wirehaired Pointer': 106,
    'Giant Schnauzer': 107,
    'Glen of Imaal Terrier': 108,
    'Golden Retriever': 109,
    'Gordon Setter': 110,
    'Great Dane': 111,
    'Great Pyrenees': 112,
    'Greater Swiss Mountain Dog': 113,
    'Greyhound': 114,
    'Harrier': 115,
    'Havanese': 116,
    'Hound': 117,
    'Hovawart': 118,
    'Husky': 119,
    'Ibizan Hound': 120,
    'Illyrian Sheepdog': 121,
    'Irish Setter': 122,
    'Irish Terrier': 123,
    'Irish Water Spaniel': 124,
    'Irish Wolfhound': 125,
    'Italian Greyhound': 126,
    'Italian Spinone': 127,
    'Jack Russell Terrier': 128,
    'Jack Russell Terrier (Parson Russell Terrier)': 129,
    'Japanese Chin': 130,
    'Jindo': 131,
    'Kai Dog': 132,
    'Karelian Bear Dog': 133,
    'Keeshond': 134,
    'Kerry Blue Terrier': 135,
    'Kishu': 136,
    'Klee Kai': 137,
    'Komondor': 138,
    'Kuvasz': 139,
    'Kyi Leo': 140,
    'Labrador Retriever': 141,
    'Lakeland Terrier': 142,
    'Lancashire Heeler': 143,
    'Leonberger': 144,
    'Lhasa Apso': 145,
    'Lowchen': 146,
    'Maltese': 147,
    'Manchester Terrier': 148,
    'Maremma Sheepdog': 149,
    'Mastiff': 150,
    'McNab': 151,
    'Miniature Pinscher': 152,
    'Mountain Cur': 153,
    'Mountain Dog': 154,
    'Munsterlander': 155,
    'Neapolitan Mastiff': 156,
    'New Guinea Singing Dog': 157,
    'Newfoundland Dog': 158,
    'Norfolk Terrier': 159,
    'Norwegian Buhund': 160,
    'Norwegian Elkhound': 161,
    'Norwegian Lundehund': 162,
    'Norwich Terrier': 163,
    'Nova Scotia Duck-Tolling Retriever': 164,
    'Old English Sheepdog': 165,
    'Otterhound': 166,
    'Papillon': 167,
    'Patterdale Terrier (Fell Terrier)': 168,
    'Pekingese': 169,
    'Peruvian Inca Orchid': 170,
    'Petit Basset Griffon Vendeen': 171,
    'Pharaoh Hound': 172,
    'Pit Bull Terrier': 173,
    'Plott Hound': 174,
    'Podengo Portugueso': 175,
    'Pointer': 176,
    'Polish Lowland Sheepdog': 177,
    'Pomeranian': 178,
    'Poodle': 179,
    'Portuguese Water Dog': 180,
    'Presa Canario': 181,
    'Pug': 182,
    'Puli': 183,
    'Pumi': 184,
    'Rat Terrier': 185,
    'Redbone Coonhound': 186,
    'Retriever': 187,
    'Rhodesian Ridgeback': 188,
    'Rottweiler': 189,
    'Saint Bernard': 190,
    'Saluki': 191,
    'Samoyed': 192,
    'Sarplaninac': 193,
    'Schipperke': 194,
    'Schnauzer': 195,
    'Scottish Deerhound': 196,
    'Scottish Terrier Scottie': 197,
    'Sealyham Terrier': 198,
    'Setter': 199,
    'Shar Pei': 200,
    'Sheep Dog': 201,
    'Shepherd': 202,
    'Shetland Sheepdog Sheltie': 203,
    'Shiba Inu': 204,
    'Shih Tzu': 205,
    'Siberian Husky': 206,
    'Silky Terrier': 207,
    'Skye Terrier': 208,
    'Sloughi': 209,
    'Smooth Fox Terrier': 210,
    'South Russian Ovtcharka': 211,
    'Spaniel': 212,
    'Spitz': 213,
    'Staffordshire Bull Terrier': 214,
    'Standard Poodle': 215,
    'Sussex Spaniel': 216,
    'Swedish Vallhund': 217,
    'Terrier': 218,
    'Thai Ridgeback': 219,
    'Tibetan Mastiff': 220,
    'Tibetan Spaniel': 221,
    'Tibetan Terrier': 222,
    'Tosa Inu': 223,
    'Toy Fox Terrier': 224,
    'Treeing Walker Coonhound': 225,
    'Vizsla': 226,
    'Weimaraner': 227,
    'Welsh Corgi': 228,
    'Welsh Springer Spaniel': 229,
    'Welsh Terrier': 230,
    'West Highland White Terrier Westie': 231,
    'Wheaten Terrier': 232,
    'Whippet': 233,
    'White German Shepherd': 234,
    'Wire Fox Terrier': 235,
    'Wire-haired Pointing Griffon': 236,
    'Wirehaired Terrier': 237,
    'Xoloitzcuintle/Mexican Hairless': 238,
    'Yellow Labrador Retriever': 239,
    'Yorkshire Terrier Yorkie': 240,
    'Mixed Breed': 307
    }

cat_dict = {
    'Abyssinian': 241,
    'American Curl': 242,
    'American Shorthair': 243,
    'American Wirehair': 244,
    'Applehead Siamese': 245,
    'Balinese': 246,
    'Bengal': 247,
    'Birman': 248,
    'Bobtail': 249,
    'Bombay': 250,
    'British Shorthair': 251,
    'Burmese': 252,
    'Burmilla': 253,
    'Calico': 254,
    'Canadian Hairless': 255,
    'Chartreux': 256,
    'Chausie': 257,
    'Chinchilla': 258,
    'Cornish Rex': 259,
    'Cymric': 260,
    'Devon Rex': 261,
    'Dilute Calico': 262,
    'Dilute Tortoiseshell': 263,
    'Domestic Long Hair': 264,
    'Domestic Medium Hair': 265,
    'Domestic Short Hair': 266,
    'Egyptian Mau': 267,
    'Exotic Shorthair': 268,
    'Extra-Toes Cat (Hemingway Polydactyl)': 269,
    'Havana': 270,
    'Himalayan': 271,
    'Japanese Bobtail': 272,
    'Javanese': 273,
    'Korat': 274,
    'LaPerm': 275,
    'Maine Coon': 276,
    'Manx': 277,
    'Munchkin': 278,
    'Nebelung': 279,
    'Norwegian Forest Cat': 280,
    'Ocicat': 281,
    'Oriental Long Hair': 282,
    'Oriental Short Hair': 283,
    'Oriental Tabby': 284,
    'Persian': 285,
    'Pixie-Bob': 286,
    'Ragamuffin': 287,
    'Ragdoll': 288,
    'Russian Blue': 289,
    'Scottish Fold': 290,
    'Selkirk Rex': 291,
    'Siamese': 292,
    'Siberian': 293,
    'Silver': 294,
    'Singapura': 295,
    'Snowshoe': 296,
    'Somali': 297,
    'Sphynx (hairless cat)': 298,
    'Tabby': 299,
    'Tiger': 300,
    'Tonkinese': 301,
    'Torbie': 302,
    'Tortoiseshell': 303,
    'Turkish Angora': 304,
    'Turkish Van': 305,
    'Tuxedo': 306
}