import json

# Load the dictionary from the JSON file
with open('user_info.json', 'r') as file:
    user_info = json.load(file)

# Access the value for 'name'
name_value = user_info.get('name', 'Key not found')
print(name_value)
print(user_info.get('age'))


