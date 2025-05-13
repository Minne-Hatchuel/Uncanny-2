ingredients = ['egg', 'tomato', 'feta cheese', 'salt', 'pepper', 'bread', 'milk', 'sugar', 'pasta', 'pesto', 'arugula', 'lemon', 'olive oil', 'cucumber', 'onion', 'red wine vinegar', 'parmesan cheese', 'butter', 'bacon', 'bell pepper', 'cumin', 'coriander', 'paprika', 'flour', 'chocolate', 'baking powder', 'rice paper', 'extra-firm tofu', 'carrot', 'avocado', 'mint', 'cabbage', 'garlic', 'dijon mustard', 'romaine lettuce', 'quinoa', 'cherry tomatoes', 'potato', 'leek', 'vegetable bouillon cube', 'vanilla extract', 'yeast', 'cinnamon', 'powdered sugar']

recipeIngredients = {'Greek omelette': ['egg', 'tomato', 'feta cheese', 'pepper', 'salt'],
    'French toast': ['egg', 'bread', 'milk', 'sugar'],
    'Pancakes': ['flour', 'butter', 'milk', 'egg', 'baking powder', 'sugar', 'vanilla extract'],
    'Crepes': ['flour', 'sugar', 'butter', 'egg', 'milk'],
    'Italian pasta salad': ['pasta', 'tomato', 'pesto', 'arugula', 'olive oil', 'lemon', 'pepper', 'salt'],
    'Greek salad': ['cucumber', 'tomato', 'onion', 'feta cheese', 'olive oil', 'red wine vinegar', 'salt', 'pepper'],
    'Spring rolls': ['rice paper', 'extra-firm tofu', 'carrot', 'cucumber', 'avocado', 'mint', 'cabbage'],
    'Caesar salad': ['bread', 'olive oil', 'parmesan cheese', 'garlic', 'dijon mustard', 'red wine vinegar', 'salt', 'pepper', 'romaine lettuce'],
    'Pasta carbonara': ['pasta', 'egg', 'parmesan cheese', 'butter', 'bacon', 'salt', 'pepper'],
    'Shakshuka': ['egg', 'tomato', 'bell pepper', 'onion', 'olive oil', 'salt', 'pepper', 'coriander', 'cumin', 'paprika'],
    'Quinoa bowl': ['quinoa', 'egg', 'cherry tomatoes', 'avocado', 'salt', 'pepper', 'olive oil', 'lemon'],
    'Vegetable soup': ['onion', 'carrot', 'potato', 'leek', 'salt', 'pepper', 'vegetable bouillon cube'], 
    'Chocolate cake': ['egg', 'sugar', 'flour', 'butter', 'chocolate', 'baking powder'],
    'Lemon cake': ['egg', 'sugar', 'flour', 'butter', 'lemon', 'baking powder'],
    'Chocolate chip cookies': ['butter', 'sugar', 'vanilla extract', 'egg', 'flour', 'baking powder', 'chocolate'],
    'Cinnamon rolls': ['milk', 'sugar', 'yeast', 'butter', 'egg', 'flour', 'cinnamon', 'powdered sugar']
}

recipeNames = ['Greek omelette', 'French toast', 'Pancakes', 'Crepes', 'Italian pasta salad', 'Greek salad', 'Spring rolls', 'Caesar salad', 'Pasta carbonara', 'Shakshuka', 'Quinoa bowl', 'Vegetable soup', 'Chocolate cake', 'Lemon cake', 'Chocolate chip cookies', 'Cinnamon rolls']


recipeInformation = {
    "Greek omelette": {
        'type': 'breakfast',
        'cookingTimeMinutes': 5,
        'difficulty': 'easy',
        'dishes': 2,
        'servings': 1, 
        'instructions': 'In a bowl, whisk together 2 eggs '
    },
    "French toast": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1,
        'description': '...',
        'instructions': '...'
    },
    "Pancakes": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1,
        'description': '...',
        'instructions': '...'
    },
    "Crepes": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1, 
        'description': '...',
        'instructions': '...'
    },
    "Italian pasta salad": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1,
        'description': '...',
        'instructions': '...'
    },
    "Greek salad": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1, 
        'description': '...',
        'instructions': '...'
    },
    "Spring rolls": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1, 
        'description': '...',
        'instructions': '...'
    },
    "Caesar salad": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1, 
        'description': '...',
        'instructions': '...'
    },  
    "Pasta carbonara": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1,
        'description': '...',
        'instructions': '...'
    },
    "Shakshuka": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1,
        'description': '...',
        'instructions': '...'
    },
    "Quinoa bowl": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1, 
        'description': '...',
        'instructions': '...'
    },
    "Vegetable soup": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1,  
        'description': '...',
        'instructions': '...'
    },
    "Chocolate cake": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1, 
        'description': '...',
        'instructions': '...'
    },
    "Lemon cake": {'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1,
        'description': '...',
        'instructions': '...'
    },
    "Chocolate chip cookies": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1, 
        'description': '...',
        'instructions': '...'
    },
    "Cinnamon rolls": {
        'type': 'breakfast',
        'cookingTimeMinutes': 0,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 1, 
        'description': '...',
        'instructions': '...'}       
}
