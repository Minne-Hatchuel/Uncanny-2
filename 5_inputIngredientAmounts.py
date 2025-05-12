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

from detailedInventory import IngredientUnits

print("For this script, you will input the amount of each ingredient you have in your kitchen.")
print("Please pay attention to the units of measurement for each ingredient. For some ingredients that do not have specific measurements, you can just input if you have it or not. ")
print("Here are the ingredients and their units of measurement:")

for ingredient in detailedIngredients.keys():
    if ingredient not in IngredientUnits:
        print(f"Warning: {ingredient} does not have a specified unit of measurement.")
    else:
        print(f"{ingredient}: {IngredientUnits[ingredient]}")

print("\nNow, please input the amount of each ingredient you have. If you do not have an ingredient, just input 0.")

for ingredient in detailedIngredients.keys():
    while True:
        try:
            amount = input(f"How much {ingredient} do you have? Answer in units of {IngredientUnits[ingredient]}: ")
            if amount.strip() == "":
                raise ValueError("Input cannot be empty.")
            detailedIngredients[ingredient] = int(amount)  # Convert input to integer
            break
        except ValueError as e:
            print("Invalid input. Please enter a valid integer.")

print("\nHere are the amounts of ingredients you have:")
for ingredient, amount in detailedIngredients.items():
    print(f"- {ingredient}: {amount} {IngredientUnits[ingredient]}")

print("\nWould you like to make any changes to your ingredient amounts? (yes/no)")
while True:
    change = input().strip().lower()
    if change == 'yes':
        while True: 
            ingredient_to_change = input("Enter the ingredient you want to change: ").strip()
            if ingredient_to_change in detailedIngredients:
                while True:
                    try:
                        amount = input(f"How much {ingredient_to_change} do you have? Answer in units of {IngredientUnits[ingredient_to_change]}: ")
                        if amount.strip() == "":
                            raise ValueError("Input cannot be empty.")
                        detailedIngredients[ingredient_to_change] = int(amount)  # Convert input to integer
                        break
                    except ValueError as e:
                        print("Invalid input. Please enter a valid integer.")
                print(f"Updated {ingredient_to_change} to {amount} {IngredientUnits[ingredient_to_change]}.")
                
                print("\nHere are the updated amounts of ingredients:")
                for ingredient, amount in detailedIngredients.items():
                    print(f"- {ingredient}: {amount} {IngredientUnits[ingredient]}")
                
                print("\nWould you like to make more changes? (yes/no)")
                continue_changes = input().strip().lower()
                if continue_changes == 'no':
                    break  
            else:
                print("Ingredient not found in your list.")
        break  
    elif change == 'no':
        break
    else:
        print("Would you like to make a change to your list? Please enter 'yes' or 'no'.")

print("\nYour ingredient amounts have been saved to 'detailedIngredients.json'.")
print("You can now navigate to the function scripts labeled with 6.")

with open('detailedIngredients.json', 'w') as file:
    json.dump(detailedIngredients, file)