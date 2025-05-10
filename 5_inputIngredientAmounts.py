import json

detailedIngredients = {
    "egg": 0,
    "tomato": 0,
    "feta cheese": 0,
    "salt": 0,
    "pepper": 0, 
    "bread": 0, 
    "milk": 0, 
    "sugar": 0,
    "pasta": 0, 
    "pesto": 0, 
    "arugula": 0, 
    "lemon": 0, 
    "olive oil": 0, 
    "cucumber": 0, 
    "onion": 0,
    "red wine vinegar": 0, 
    "parmesan cheese": 0, 
    "butter": 0, 
    "bacon": 0, 
    "bell pepper": 0,
    "cumin": 0, 
    "coriander": 0, 
    "paprika": 0, 
    "flour": 0, 
    "baking powder": 0
    # Add more ingredients as needed
}

with open('detailedIngredients.json', 'w') as file:
    json.dump(detailedIngredients, file)
