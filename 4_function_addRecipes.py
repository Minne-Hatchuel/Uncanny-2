import json

from inventory import recipeNames, recipeIngredients, recipeInformation

modifiedRecipeNames = recipeNames
modifiedRecipeIngredients = recipeIngredients
modifiedRecipeInformation = recipeInformation

# Function to add a new recipe
def add_new_recipe():
    # Get user input for the new recipe
    recipe_name = input("Enter the name of the recipe (for example, 'Toast'): ")
    recipe_ingredients = input("Enter the ingredients (comma-separated): ").split(",")
    
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