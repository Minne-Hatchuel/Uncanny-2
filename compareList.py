import json

# Load the dictionary from the JSON file
with open('user_info.json', 'r') as file:
    userInfo = json.load(file)

# Access the value for 'name'
name_value = userInfo.get('name', 'Key not found')
print(name_value)
print(userInfo.get('age'))


hello = "Hello, World!"