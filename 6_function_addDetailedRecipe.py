import json

from inventory import recipeNames, recipeIngredients, recipeInformation
from detailedInventory import detailedRecipeIngredients

# Define the list of allowed ingredients
ingredients = set()
for ing_list in recipeIngredients.values():
    ingredients.update(ing_list)
ingredients = list(ingredients)

# Try to load existing recipes so we don't overwrite them
try:
    with open('modifiedDetailedRecipes.json', 'r') as file:
        modifiedDetailedRecipes = json.load(file)
        modifiedRecipeNames = modifiedDetailedRecipes.get("modifiedRecipeNames", [])
        modifiedRecipeIngredients = modifiedDetailedRecipes.get("modifiedRecipeIngredients", {})
        modifiedRecipeInformation = modifiedDetailedRecipes.get("modifiedRecipeInformation", {})
except (FileNotFoundError, json.JSONDecodeError):
    modifiedRecipeNames = recipeNames.copy()
    modifiedRecipeIngredients = detailedRecipeIngredients.copy()
    modifiedRecipeInformation = recipeInformation.copy()

# Function to add a new recipe
def add_new_recipe():
    # Show all possible ingredients
    print("Possible ingredients:")
    print(", ".join(ingredients))
    print("Only add ingredients from the above list.")

    # Get user input for the new recipe
    recipe_name = input("Enter the name of the recipe (for example, 'Toast'): ")

    # Get ingredients and their amounts
    detailed_ingredients = {}
    print("Enter the ingredients and the nonnegative integer amount needed for each.")
    print("Type 'done' when finished.")
    while True:
        ing = input("Ingredient name (or 'done'): ").strip()
        if ing == "done":
            if detailed_ingredients:
                break
            else:
                print("Please enter at least one ingredient.")
                continue
        if ing not in ingredients:
            print("Ingredient not in allowed list. Try again.")
            continue
        while True:
            try:
                amt = int(input(f"Amount needed for {ing}: "))
                if amt >= 0:
                    detailed_ingredients[ing] = amt
                    break
                else:
                    print("Please enter a nonnegative integer.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Get user input for the meal type
    print("Select the meal type:")
    print("1 - Breakfast")
    print("2 - Cold dish")
    print("3 - Warm dish")
    print("4 - Baked good")
    while True:
        try:
            meal_type = int(input("Enter the meal type (1-4): "))
            if meal_type in [1, 2, 3, 4]:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get user input for the difficulty level
    print("Select the difficulty level:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Difficult")
    print("4 - Master Chef")
    while True:
        try:
            difficulty_level = int(input("Enter the difficulty level (1-4): "))
            if difficulty_level in [1, 2, 3, 4]:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get user input for cooking time, number of pots/pans, servings, and instructions
    cooking_time = input("Enter the cooking time in minutes: ")
    while True:
        try:
            dishes = int(input("Enter the number of pots or pans needed: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        try:
            servings = int(input("Enter the number of servings: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    instructions = input("Enter the instructions: ")

    # Create the recipe information dictionary
    recipeInformationDict = {
        "type": meal_type,
        "cookingTimeMinutes": cooking_time,
        "difficulty": difficulty_level,
        "dishes": dishes,
        "servings": servings,
        "instructions": instructions
    }
            
    # Add the new recipe to the modified data (append or update)
    if recipe_name not in modifiedRecipeNames:
        modifiedRecipeNames.append(recipe_name)
    modifiedRecipeIngredients[recipe_name] = detailed_ingredients  # now a dict of ingredient: amount
    modifiedRecipeInformation[recipe_name] = recipeInformationDict

    print(f"Recipe '{recipe_name}' added successfully!!")

# Call the function to add a new recipe
add_new_recipe()

modifiedDetailedRecipes = {
    "modifiedRecipeNames": modifiedRecipeNames,
    "modifiedRecipeIngredients": modifiedRecipeIngredients,
    "modifiedRecipeInformation": modifiedRecipeInformation
}

with open('modifiedDetailedRecipes.json', 'w') as file:
    json.dump(modifiedDetailedRecipes, file, indent=4)