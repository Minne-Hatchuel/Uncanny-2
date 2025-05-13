import json

from inventory import recipeNames, recipeIngredients, recipeInformation

# Define the list of allowed ingredients
ingredients = set()
for ing_list in recipeIngredients.values():
    ingredients.update(ing_list)
ingredients = list(ingredients)

modifiedRecipeNames = recipeNames
modifiedRecipeIngredients = recipeIngredients
modifiedRecipeInformation = recipeInformation


# Function to add a new recipe
def add_new_recipe():

    # Show all possible ingredients
    print("Possible ingredients:")
    print(", ".join(ingredients))
    print("Only add ingredients from the above list.")

    # Get user input for the new recipe
    recipe_name = input("Enter the name of the recipe (for example, 'Toast'): ")
   
   # Loop until all entered ingredients are valid
    while True:
        recipe_ingredients = input("Enter the ingredients (comma-separated and without caps): ").split(",")
        recipe_ingredients = [i.strip() for i in recipe_ingredients]
        if all(ing in ingredients for ing in recipe_ingredients):
            break
        else:
            print("One or more ingredients are not in the allowed list. Please try again.")

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
    recipeInformation = {
        "type": meal_type,
        "cookingTimeMinutes": cooking_time,
        "difficulty": difficulty_level,
        "dishes": dishes,
        "servings": servings,
        "instructions": instructions
    }
            
    # Add the new recipe to the modified data
    modifiedRecipeNames.append(recipe_name)
    modifiedRecipeIngredients[recipe_name] = [ingredient.strip() for ingredient in recipe_ingredients]
    modifiedRecipeInformation[recipe_name] = recipeInformation

    print(f"Recipe '{recipe_name}' added successfully!!")

# Call the function to add a new recipe
add_new_recipe()


modifiedRecipes = {
    "modifiedRecipeNames": modifiedRecipeNames,
    "modifiedRecipeIngredients": modifiedRecipeIngredients,
    "modifiedRecipeInformation": modifiedRecipeInformation
}

with open('modifiedRecipes.json', 'w') as file:
    json.dump(modifiedRecipes, file, indent=4) 