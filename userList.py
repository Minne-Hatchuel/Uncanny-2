import json

# List of ingredients to ask the user about
ingredients = [
    "egg", "tomato", "feta cheese", "salt", "pepper", "bread", "milk", "sugar",
    "pasta", "pesto", "arugula", "lemon", "olive oil", "cucumber", "onion",
    "red wine vinegar", "parmesan cheese", "butter", "bacon", "bell pepper",
    "cumin", "coriander", "paprika", "flour", "baking powder"
]

userIngredients = {}

def get_user_input(ingredient):
    while True:
        response = input(f"Do you have {ingredient}? Enter 1 for Yes or 0 for No: ")
        if response in ['1', '0']:
            return response == '1'  # Return True for '1', False for '0'
        else:
            print("Invalid input. Please enter 1 for Yes or 0 for No.")

for ingredient in ingredients:
    userIngredients[ingredient] = get_user_input(ingredient)


print("\nHere are the ingredients you have:")
for ingredient, has_it in userIngredients.items():
    print(f"- {ingredient}: {'Yes' if has_it else 'No'}")

with open('userIngredients.json', 'w') as file:
    json.dump(userIngredients, file)

print("\nYour ingredient list has been saved to 'userIngredients.json'.")