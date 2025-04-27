import json

userIngredients = 

egg = input("Do you have egg? 1(yes)/0(no) ")
if egg == '1':
    userIngredients['egg'] = True
else:
    userIngredients['egg'] = False
tomato = input("Do you have tomato? 1(yes)/0(no) ")
if tomato == '1':
    userIngredients['tomato'] = True
else:               
    userIngredients['tomato'] = False       
feta_cheese = input("Do you have feta cheese? 1(yes)/0(no) ")
if feta_cheese == '1':
    userIngredients['feta_cheese'] = True
else:
    userIngredients['feta_cheese'] = False
salt = input("Do you have salt? 1(yes)/0(no) ")
if salt == '1':
    userIngredients['salt'] = True
else:
    userIngredients['salt'] = False
pepper = input("Do you have pepper? 1(yes)/0(no) ")
if pepper == '1':
    userIngredients['pepper'] = True
else:
    userIngredients['pepper'] = False
bread = input("Do you have bread? 1(yes)/0(no) ")
if bread == '1':
    userIngredients['bread'] = True
else:
    userIngredients['bread'] = False
milk = input("Do you have milk? 1(yes)/0(no) ")
if milk == '1':
    userIngredients['milk'] = True
else:
    userIngredients['milk'] = False
sugar = input("Do you have sugar? 1(yes)/0(no) ")
if sugar == '1':
    userIngredients['sugar'] = True
else:
    userIngredients['sugar'] = False            
pasta = input("Do you have pasta? 1(yes)/0(no) ")
if pasta == '1':
    userIngredients['pasta'] = True
else:
    userIngredients['pasta'] = False
pesto = input("Do you have pesto? 1(yes)/0(no) ")
if pesto == '1':
    userIngredients['pesto'] = True
else:
    userIngredients['pesto'] = False
arugula = input("Do you have arugula? 1(yes)/0(no) ")   
if arugula == '1':
    userIngredients['arugula'] = True
else:
    userIngredients['arugula'] = False
lemon = input("Do you have lemon? 1(yes)/0(no) ")
if lemon == '1':
    userIngredients['lemon'] = True
else:
    userIngredients['lemon'] = False
olive_oil = input("Do you have olive oil? 1(yes)/0(no) ")
if olive_oil == '1':
    userIngredients['olive_oil'] = True
else:
    userIngredients['olive_oil'] = False
cucumber = input("Do you have cucumber? 1(yes)/0(no) ") 
if cucumber == '1':
    userIngredients['cucumber'] = True
else:
    userIngredients['cucumber'] = False
onion = input("Do you have onion? 1(yes)/0(no) ")
if onion == '1':
    userIngredients['onion'] = True
else:
    userIngredients['onion'] = False
red_wine_vinegar = input("Do you have red wine vinegar? 1(yes)/0(no) ")     
if red_wine_vinegar == '1':
    userIngredients['red_wine_vinegar'] = True
else:
    userIngredients['red_wine_vinegar'] = False
parmesan_cheese = input("Do you have parmesan cheese? 1(yes)/0(no) ")
if parmesan_cheese == '1':
    userIngredients['parmesan_cheese'] = True
else:
    userIngredients['parmesan_cheese'] = False
butter = input("Do you have butter? 1(yes)/0(no) ")
if butter == '1':
    userIngredients['butter'] = True
else:
    userIngredients['butter'] = False
bacon = input("Do you have bacon? 1(yes)/0(no) ")
if bacon == '1':
    userIngredients['bacon'] = True
else:
    userIngredients['bacon'] = False
bell_pepper = input("Do you have bell pepper? 1(yes)/0(no) ")
if bell_pepper == '1':
    userIngredients['bell_pepper'] = True
else:
    userIngredients['bell_pepper'] = False
cumin = input("Do you have cumin? 1(yes)/0(no) ")
if cumin == '1':
    userIngredients['cumin'] = True
else:
    userIngredients['cumin'] = False
coriander = input("Do you have coriander? 1(yes)/0(no) ")
if coriander == '1':
    userIngredients['coriander'] = True
else:
    userIngredients['coriander'] = False        
paprika = input("Do you have paprika? 1(yes)/0(no) ")
if paprika == '1':
    userIngredients['paprika'] = True
else:
    userIngredients['paprika'] = False
flour = input("Do you have flour? 1(yes)/0(no) ")
if flour == '1':
    userIngredients['flour'] = True
else:
    userIngredients['flour'] = False        
baking_powder = input("Do you have baking powder? 1(yes)/0(no) ")
if baking_powder == '1':
    userIngredients['baking_powder'] = True
else:
    userIngredients['baking_powder'] = False


# Print the dictionary
print(userIngredients)

# Save the dictionary to a JSON file
with open('userIngredients.json', 'w') as file:
    json.dump(userIngredients, file)

print("User info saved to userIngredients.json")