from inventory import ingredients, recipeIngredients

response = input(f"Would you like to view the ingredient list or look up recipes that include a specific ingredient? Enter 1 to see the full ingredient list or 2 to look up recipes with a specific ingredient: ")
if response == '1':
    print(ingredients)
elif response == '2':
    ingredientName = input(f"Enter the ingredient you want to look up (all lower case): ").strip()
    if ingredientName in ingredients:
        print(f"{ingredientName} is in the ingredient list.")
        # Show all recipes that include this ingredient
        recipes_with_ingredient = [recipe for recipe, ingr_list in recipeIngredients.items() if ingredientName in ingr_list]
        if recipes_with_ingredient:
            print(f"Recipes that include {ingredientName}:")
            for recipe in recipes_with_ingredient:
                print("-", recipe)
        else:
            print(f"No recipes include {ingredientName}.")
    else:
        print(f"{ingredientName} is not in the ingredient list.")