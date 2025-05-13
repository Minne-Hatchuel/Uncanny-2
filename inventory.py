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
        'cookingTimeMinutes': 10,
        'difficulty': 'easy',
        'dishes': 2,
        'servings': 1, 
        'instructions': '1) In a bowl, whisk your eggs.\n\n2) Add in chopped tomatoes and mix well.\n\n3) Heat up an oiled pan. Once the pan is hot, pour in your egg and tomato mixture.\n\n4) When the eggs start solidifying, add in some crumbled feta cheese.\n\n5) Cook the omeletter to your liking, making sure to mix the eggs frequently so that they cook evenly.\n\n6) Season the omelette with salt and pepper.'
    },
    "French toast": {
        'type': 'breakfast',
        'cookingTimeMinutes': 5,
        'difficulty': 'easy',
        'dishes': 2,
        'servings': 2,
        'instructions': '1) In a bowl, whisk your eggs with the milk.\n\n2) Add your slices of bread in the egg and milk mixture, and let them imbibe until soft.\n\n3) Heat up an oiled pan. Once the pan is hot, add in your pieces of bread (add in the wet bread only, dont pour the mixture into the pan).\n\n4) Flip over the bread slices when one side looks golden brown. Your French toast is ready when both sides are golden brown but the bread is tender on the inside.\n\n5) You may serve your French toast with some maple syrup or powdered sugar.'
    },
    "Pancakes": {
        'type': 'breakfast',
        'cookingTimeMinutes': 20,
        'difficulty': 'medium',
        'dishes': 2,
        'servings': 4,
        'instructions': '1) In a bowl, add in your flour, baking powder, and sugar. Mix with a whisk.\n\n2) Add in your eggs and the melted butter. Make sure the butter has had time to cool so that it doesnt cook the eggs.\n\n3) Add in your milk, little by little, and mix well to make sure the batter remains homogeneous.\n\n4) Heat up an oiled pan. Once the pan is hot, pour in one or multiple ladles of batter (depending on how big you want your pancakes to be).\n\n5) When small bubbles begin to appear all over the surface of your pancakes, flip them and let them cook one more minute (until the other side is golden brown).\n\n6) You may serve your pancakes with fruit, syrup, and/or powdered sugar.'
    },
    "Crepes": {
        'type': 'breakfast',
        'cookingTimeMinutes': 15,
        'difficulty': 'medium',
        'dishes': 2,
        'servings': 4, 
        'instructions': '1) In a bowl, add in your flour.\n\n2) Add in your eggs, one by one, and mix them in as well as possible (the batter will be very thick, thats normal).\n\n3) Then, add in your sugar and melted butter.\n\n4) Add in your milk, a little at a time, and mix well to make sure the dough remains homogeneous.\n\n5) Heat up an oiled pan (preferably a crepe pan). Once the pan is hot, pour in a ladle of the batter and immediately pick up the pan and tilt it as needed so that the batter evenly covers the pan (it should be a thin layer).\n\n6) Once the edges of the crepe begin to brown, flip the crepe and cook it for 30 more seconds.\n\n7) Serve your crepes with granulated sugar.'
    },
    "Italian pasta salad": {
        'type': 'cold dish',
        'cookingTimeMinutes': 20,
        'difficulty': 'easy',
        'dishes': 2,
        'servings': 2,
        'instructions': '1) Boil some water to cook your pasta.\n\n2) While your water heats up, chop up your tomatoes and arugula.\n\n3) Cook your pasta for 10-15 minutes, depending on whether you like it al dente or not.\n\n4) Once the pasta is cooked, strain it and prepare the dressing for the salad while it cools down. In a bowl, add some olive oil, lemon, pepper, salt, and a teaspoon of pesto.\n\n5) Once the pasta has cooled down, add it to the bowl as well as the chopped tomatoes and arugula. Mix well and serve.'
    },
    "Greek salad": {
        'type': 'cold dish',
        'cookingTimeMinutes': 5,
        'difficulty': 'easy',
        'dishes': 1,
        'servings': 2, 
        'instructions': '1) Chop up your cucumber, tomatoes, and onion.\n\n2) In a bowl, mix some olive oil, red wine vinegar, salt, and pepper for the dressing.\n\n3) Add in your chopped vegetables as well as some feta cubes.\n\n4) Mix well before serving.'
    },
    "Spring rolls": {
        'type': 'cold dish',
        'cookingTimeMinutes': 10,
        'difficulty': 'medium',
        'dishes': 1,
        'servings': 1, 
        'instructions': '1) In a large bowl or a plate with a raised rim, add some water and soak your rice paper sheets, one at a time.\n\n2) Chop up your tofu, carrot, cucumber, avocado, and cabbage into strips.\n\n3) Lay out your rice paper on a flat surface. In the middle, put some of your vegetables, tofu, and some mint.\n\n4) Fold the sides of the rice paper over and the roll it from the top down in order to form a roll.\n\n5) Repeat these steps until you get 3-4 spring rolls and serve.'
    },
    "Caesar salad": {
        'type': 'cold dish',
        'cookingTimeMinutes': 15,
        'difficulty': 'medium',
        'dishes': 2,
        'servings': 2, 
        'instructions': '1) In a bowl, mix some olive oil, dijon mustard, red wine vinegar, salt, pepper, minced garlic, and grated parmesan cheese. Mix well to create a thick dressing.\n\n2) Heat up an oiled pan. Chop up your bread slices into cubes and, once the pan is hot, add them in.\n\n3) While the croutons are cooking, wash and chop up your romaine lettuce.\n\n4) Once the croutons are golden brown and crunchy, assemble your salad by adding the lettuce, croutons, and some more grated parmesan to the bowl. Mix well and serve.'
    },  
    "Pasta carbonara": {
        'type': 'warm dish',
        'cookingTimeMinutes': 15,
        'difficulty': 'medium',
        'dishes': 3,
        'servings': 2,
        'instructions': '1) Boil some water to cook your pasta. While the water heats up, add some olive oil, butter, salt, pepper, grated parmesan cheese, and an egg yolk to a bowl.\n\n2) While your pasta is cooking, heat up a pan and cooked your chopped bacon until crispy. Add them to the bowl.\n\n3) When the pasta is cooked, before straining it, take a ladle of the pasta water and add it to the bowl. Mix well until the ingredients combine into a thick sauce. Add more water if necessary.\n\n4) Add your pasta to the sauce, mix well to combine, and serve.'
    },
    "Shakshuka": {
        'type': 'warm dish',
        'cookingTimeMinutes': 40,
        'difficulty': 'hard',
        'dishes': 1,
        'servings': 4,
        'instructions': 'Heat up an oiled pan. Chope up your onion and cook it in the pan until slightlmy golden.\n\n2) Add in your chopped tomatoes and bell peppers, cover the pan and let simmer.\n\n3) Once the tomato, onion, bell pepper mixture begins looking like a thick sauce, add in your salt, pepper, coriander, cumin, paprika, and mix well.\n\n4) Crack your eggs into the sauce and cover the pan until cooked. Serve.'
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
