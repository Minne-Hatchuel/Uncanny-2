import json

# Load the dictionary from the JSON file
with open('userIngredients.json', 'r') as file:
    userIngredients = json.load(file)

yesIngredients = []
for key, value in userIngredients.items():
    if value == True:
        yesIngredients.append(key)

print(yesIngredients)

from inventory import recipeIngredients

def compareList(yesIngredients, recipeIngredients):
    recipeList = []
    for key, value in recipeIngredients.items():
        if set(value) == set(yesIngredients):
            recipeList.append(key)
        elif set(value).issubset(set(yesIngredients)):
            recipeList.append(key)
    return recipeList

def showCompareList(recipeList):
    if len(recipeList) > 0:
        print(recipeList)
    elif len(recipeList) == 0:
        print("No recipes found")





