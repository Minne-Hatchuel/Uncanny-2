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
    
    # Get user input for the difficulty level
    print("Select the difficulty level:")
    print("0 - Easy")
    print("1 - Medium")
    print("2 - Difficult")
    print("3 - Master Chef")
    while True:
        try:
            difficulty_level = int(input("Enter the difficulty level (0-3): "))
            if difficulty_level in [0, 1, 2, 3]:
                break
            else:
                print("Invalid input. Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    # Add the new recipe to the modified data
    modifiedRecipeNames.append(recipe_name)
    modifiedRecipeIngredients[recipe_name] = [ingredient.strip() for ingredient in recipe_ingredients]
    modifiedRecipeInformation[recipe_name] = recipe_information

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