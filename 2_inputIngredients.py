import json

# List of ingredients to ask the user about
ingredients = [
    "egg", "tomato", "feta cheese", "salt", "pepper", "bread", "milk", "sugar",
    "pasta", "pesto", "arugula", "lemon", "olive oil", "cucumber", "onion",
    "red wine vinegar", "parmesan cheese", "butter", "bacon", "bell pepper",
    "cumin", "coriander", "paprika", "flour", "baking powder"
]

userIngredients = {}

print("It is time to input your ingredients. Please answer the following questions with 1 for Yes and 0 for No.\n")

def get_user_input(ingredient):
    while True:
        response = input(f"Do you have {ingredient}? Enter 1 for Yes or 0 for No: ")
        if response in ['1', '0']:
            return response == '1'  # Return True for '1', False for '0'
        else:
            print("Invalid input. Please enter 1 for Yes or 0 for No.")

for ingredient in ingredients:
    userIngredients[ingredient] = get_user_input(ingredient)


print("\nHere are the ingredients you have:")
for ingredient, has_it in userIngredients.items():
    print(f"- {ingredient}: {'Yes' if has_it else 'No'}")



print("\nWould you like to make any changes to your ingredient list? (yes/no)")
while True:
    change = input().strip().lower()
    if change == 'yes':
        while True: 
            ingredient_to_change = input("Enter the ingredient you want to change: ").strip()
            if ingredient_to_change in userIngredients:
                new_value = get_user_input(ingredient_to_change)
                userIngredients[ingredient_to_change] = new_value
                print(f"Updated {ingredient_to_change} to {'Yes' if new_value else 'No'}.")
                
                print("\nHere are the updated ingredients:")
                for ingredient, has_it in userIngredients.items():
                    print(f"- {ingredient}: {'Yes' if has_it else 'No'}")

               
                print("\nWould you like to make more changes? (yes/no)")
                continue_changes = input().strip().lower()
                if continue_changes == 'no':
                    break  
            else:
                print("Ingredient not found in your list.")
        break  
    elif change == 'no':
        break
    else:
        print("Would you like to make a change to your list? Please enter 'yes' or 'no'.")

with open('userIngredients.json', 'w') as file:
    json.dump(userIngredients, file)

print("\nYour ingredient list has been saved to 'userIngredients.json'.")
print("You can now navigate to the function scripts")


