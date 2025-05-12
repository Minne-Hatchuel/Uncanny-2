import json

from inventory import recipeNames, recipeIngredients, recipeInformation

modifiedRecipeNames = recipeNames
modifiedRecipeIngredients = recipeIngredients
modifiedRecipeInformation = recipeInformation

modifiedRecipes = {
    "modifiedRecipeNames": modifiedRecipeNames,
    "modifiedRecipeIngredients": modifiedRecipeIngredients,
    "modifiedRecipeInformation": modifiedRecipeInformation
}

with open('modifiedRecipes.json', 'w') as file:
    json.dump(modifiedRecipes, file, indent=4) 