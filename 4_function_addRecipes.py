import json

from inventory import recipeNames, recipeIngredients, recipeInformation

modifiedRecipeNames = recipeNames
modifiedRecipeIngredients = recipeIngredients
modifiedRecipeInformation = recipeInformation

# Function to add a new recipe
def add_new_recipe():
    # Get user input for the new recipe
    recipe_name = input("Enter the name of the recipe: ")
    recipe_ingredients = input("Enter the ingredients (comma-separated): ").split(",")
    recipe_information = input("Enter additional information about the recipe: ")

    # Add the new recipe to the modified data
    modifiedRecipeNames.append(recipe_name)
    modifiedRecipeIngredients[recipe_name] = [ingredient.strip() for ingredient in recipe_ingredients]
    modifiedRecipeInformation[recipe_name] = recipe_information

    print(f"Recipe '{recipe_name}' added successfully!")

# Call the function to add a new recipe
add_new_recipe()

modifiedRecipes = {
    "modifiedRecipeNames": modifiedRecipeNames,
    "modifiedRecipeIngredients": modifiedRecipeIngredients,
    "modifiedRecipeInformation": modifiedRecipeInformation
}

with open('modifiedRecipes.json', 'w') as file:
    json.dump(modifiedRecipes, file, indent=4) 