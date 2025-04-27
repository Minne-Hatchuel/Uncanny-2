import json

userIngredients = {}

# Get user input for name
name = input("What is your name? ")
userIngredients['name'] = name

# Get user input for age
age = input("What is your age? ")
userIngredients['age'] = age

# Get user input for favorite color
favorite_color = input("What is your favorite color? ")
userIngredients['favorite_color'] = favorite_color

# Print the dictionary
print(userIngredients)

# Save the dictionary to a JSON file
with open('userIngredients.json', 'w') as file:
    json.dump(userIngredients, file)

print("User info saved to userIngredients.json")