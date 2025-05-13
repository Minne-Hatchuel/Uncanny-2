import json

with open('modifiedRecipes.json', 'r') as file:
    modifiedRecipes = json.load(file)

recipeNames = modifiedRecipes["modifiedRecipeNames"]
print("Here are all possible recipes:")
for name in recipeNames:
    print("-", name)

recipe_name = input("Enter the name of the recipe you want to edit: ") 
if recipe_name not in recipeNames:
    print("Recipe not found. Please check the name and try again.")
    exit()

info_dict = modifiedRecipes["modifiedRecipeInformation"][recipe_name]
keys = list(info_dict.keys())
print("\nCurrent recipe information:")
for idx, (key, value) in enumerate(info_dict.items(), 1):
    print(f"{idx}. {key}: {value}")

print("\nWhich aspect would you like to change?")
for idx, key in enumerate(keys, 1):
    print(f"{idx}. {key}")

print(f"{len(keys)+1}. ingredient amounts")

choice = input("Enter the number corresponding to the aspect you want to change: ")
try:
    choice_idx = int(choice) - 1
    if choice_idx < 0 or choice_idx > len(keys):
        print("Invalid choice.")
        exit()
except ValueError:
    print("Invalid input.")
    exit()

if choice_idx == len(keys):
    # Edit ingredient amounts
    ingredients_dict = modifiedRecipes["modifiedRecipeIngredients"][recipe_name]
    print("\nCurrent ingredient amounts:")
    for ing, amt in ingredients_dict.items():
        print(f"{ing}: {amt}")
    print("Type the name of the ingredient you want to change, or 'done' to finish.")
    while True:
        ing_name = input("Ingredient to change (or 'done'): ").strip()
        if ing_name == "done":
            break
        if ing_name not in ingredients_dict:
            print("Ingredient not found in this recipe. Try again.")
            continue
        while True:
            new_amt = input(f"Enter new nonnegative integer amount for {ing_name}: ")
            try:
                new_amt = int(new_amt)
                if new_amt >= 0:
                    ingredients_dict[ing_name] = new_amt
                    print(f"{ing_name} updated to {new_amt}.")
                    break
                else:
                    print("Please enter a nonnegative number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    modifiedRecipes["modifiedRecipeIngredients"][recipe_name] = ingredients_dict
    print("Ingredient amounts updated successfully!")
else:
    aspect = keys[choice_idx]
    print(f"Current value for '{aspect}': {info_dict[aspect]}")

    if aspect == "type":
        print("Select the meal type:")
        print("1 - Breakfast")
        print("2 - Cold dish")
        print("3 - Warm dish")
        print("4 - Baked good")
        while True:
            new_value = input("Enter the meal type (1-4): ")
            if new_value in ["1", "2", "3", "4"]:
                info_dict[aspect] = int(new_value)
                break
            else:
                print("Invalid input. Please enter 1, 2, 3, or 4.")
    elif aspect == "difficulty":
        print("Select the difficulty level:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Difficult")
        print("4 - Master Chef")
        while True:
            new_value = input("Enter the difficulty level (1-4): ")
            if new_value in ["1", "2", "3", "4"]:
                info_dict[aspect] = int(new_value)
                break
            else:
                print("Invalid input. Please enter 1, 2, 3, or 4.")
    elif aspect in ["cookingTimeMinutes", "dishes", "servings"]:
        while True:
            new_value = input(f"Enter a nonnegative number for {aspect}: ")
            try:
                num = int(new_value)
                if num >= 0:
                    info_dict[aspect] = num
                    break
                else:
                    print("Please enter a nonnegative number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif aspect == "instructions":
        new_value = input("Enter the new instructions (you can type anything): ")
        info_dict[aspect] = new_value
    else:
        new_value = input(f"Enter the new value for {aspect}: ")
        info_dict[aspect] = new_value

    # Save the changes for info_dict
    modifiedRecipes["modifiedRecipeInformation"][recipe_name] = info_dict
    print(f"{aspect} updated successfully to a new value of {info_dict[aspect]}!")

# Save all changes
with open('modifiedRecipes.json', 'w') as file:
    json.dump(modifiedRecipes, file, indent=4)

