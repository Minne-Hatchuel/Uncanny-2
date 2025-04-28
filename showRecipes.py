from inventory import recipeNames

response = input(f"Would you like to view the recipe list? Enter 1 for Yes or 0 for No.")
if response == '1':
    print(recipeNames)


