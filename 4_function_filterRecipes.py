import json

print("You can filter recipes by the following ways:")
print("1. type (e.g., breakfast, cold dish, warm dish, baked good)")
print("2. cookingTimeMinutes (how long it takes to cook, in minutes)")
print("3. difficulty (e.g., easy, medium, difficult, master chef)")
print("4. dishes (number of pots or pans needed)")
print("5. servings (number of servings)")

filter_choice = input("Enter the number (1-5) corresponding to how you want to filter recipes: ")

with open('modifiedRecipes.json', 'r') as file:
    modifiedRecipes = json.load(file)

recipe_info = modifiedRecipes["modifiedRecipeInformation"]

if filter_choice == "1":
    print("Which type do you want to filter by?")
    print("1 - breakfast")
    print("2 - cold dish")
    print("3 - warm dish")
    print("4 - baked good")
    type_choice = input("Enter the number (1-4) for the type: ")
    type_map = {"1": "breakfast", "2": "cold dish", "3": "warm dish", "4": "baked good"}
    selected_type = type_map.get(type_choice)
    if selected_type:
        print(f"\nRecipes of type '{selected_type}':")
        for name, info in recipe_info.items():
            # Accept both string and int types for 'type'
            if str(info.get("type")).lower() == selected_type:
                print("-", name)
    else:
        print("Invalid type selection.")

elif filter_choice == "2":
    try:
        max_minutes = int(input("Enter the maximum number of minutes: "))
        print(f"\nRecipes that take {max_minutes} minutes or less:")
        for name, info in recipe_info.items():
            try:
                if int(info.get("cookingTimeMinutes", 9999)) <= max_minutes:
                    print("-", name)
            except (ValueError, TypeError):
                continue
    except ValueError:
        print("Invalid input. Please enter a number.")

elif filter_choice == "3":
    print("Which difficulty level do you want to filter by?")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Difficult")
    print("4 - Master Chef")
    diff_choice = input("Enter the number (1-4) for the difficulty: ")
    if diff_choice in ["1", "2", "3", "4"]:
        selected_diff = int(diff_choice)
        print(f"\nRecipes with difficulty level {selected_diff}:")
        for name, info in recipe_info.items():
            if info.get("difficulty") == selected_diff:
                print("-", name)
    else:
        print("Invalid difficulty selection. Please enter a number between 1 and 4.")

elif filter_choice == "4":
    try:
        num_dishes = int(input("Enter the number of pots or pans to filter by: "))
        print(f"\nRecipes that need {num_dishes} pots or pans:")
        for name, info in recipe_info.items():
            try:
                if int(info.get("dishes", -1)) == num_dishes:
                    print("-", name)
            except (ValueError, TypeError):
                continue
    except ValueError:
        print("Invalid input. Please enter a number.")

elif filter_choice == "5":
    try:
        num_servings = int(input("Enter the number of servings to filter by: "))
        print(f"\nRecipes that make {num_servings} servings:")
        for name, info in recipe_info.items():
            try:
                if int(info.get("servings", -1)) == num_servings:
                    print("-", name)
            except (ValueError, TypeError):
                continue
    except ValueError:
        print("Invalid input. Please enter a number.")