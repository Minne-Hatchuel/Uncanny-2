print ('Welcome to Minne, Tatsuya, and Alex\'s final project!')
print ('type "start" for instructions')

response = input('> ')
if response == 'start':
    print('''
        In this program, you will input ingredients that 
        you have access to and the program will provide 
        you with a list of recipes that you can make with
        those ingredients along with instruction on how to
        make them. 
        In addition this program also comes with a set of 
        extra functions:
            1. View the list of ingredients
            2. View the list of recipes
            3. Add a new recipe
            4. Edit an existing recipe
            5. Filter recipes based on preferences
        If you want to see some more detailed functionality, you
        can input how much of each ingredient you have and the
        program will provide you with a list of recipes that
        you can make with those ingredients along with 
        a few more functions: 
            1. Add detailed recipe
            2. Edit detailed recipe

        
        To get started, please navigate to the script labeled 
        "2_inputIngredients.py" and run it.
        This will allow you to input the ingredients you have
        access to.
        From there, you can use any of the scripts labeled with 
        3 or 4. 
        If you want to use the detailed recipe functions, first 
        navigate to the script labeled "5_inputIngredientAmounts.py"
        and run it. From there, you can use any of the scripts labeled with
        6. 
    ''')