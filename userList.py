import json

user_info = {}

# Get user input for name
name = input("What is your name? ")
user_info['name'] = name

# Get user input for age
age = input("What is your age? ")
user_info['age'] = age

# Get user input for favorite color
favorite_color = input("What is your favorite color? ")
user_info['favorite_color'] = favorite_color

# Print the dictionary
print(user_info)

# Save the dictionary to a JSON file
with open('user_info.json', 'w') as file:
    json.dump(user_info, file)

print("User info saved to user_info.json")