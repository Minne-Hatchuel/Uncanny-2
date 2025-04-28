from inventory import ingredients

response = input(f"Would you like to view the ingredient list or look up a specific ingredient? Enter 1 to see the full ingredient list or 2 to look up a specific ingredient.")
if response == '1':
    print(ingredients)
elif response == '2':
    ingredientName = input(f"Enter the ingredient you want to look up (all lower case): ").strip()
    if ingredientName in ingredients:
        print(f"{ingredientName} is in the ingredient list.")
    else:
        print(f"{ingredientName} is not in the ingredient list.")