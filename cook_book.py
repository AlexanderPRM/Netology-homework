from pprint import pprint
list_recipe = 'recipe.txt'

def decorated_list_dish():
    cook_book = {}
    with open(list_recipe, encoding='utf8') as recipes:
        for line in recipes:
            dish_name = line.strip()
            value = recipes.readline()
            ing_list = []
            for el in range(int(value)):
                ings = {}
                count = 0
                ingredient = recipes.readline()
                for value in ingredient.split('|'):
                    count += 1
                    value = value.strip()
                    if count == 1:
                        ings['ingredient name'] = value
                    elif count == 2:
                        ings['quantity'] = value
                    elif count == 3:
                        ings['measuer'] = value
                ing_list.append(ings)

            cook_book[dish_name] = ing_list
            recipes.readline()
        return cook_book

cook_book = decorated_list_dish()

def get_shop_list_by_dishes(dishes, person):
    dishes_ingredients = {}
    for dish in dishes:
        el = cook_book[dish]
        for ing in el:
            ings = {}
            name_ing = ''
            name_ing += ing['ingredient name']
            if not ing['ingredient name'] in dishes_ingredients.keys():
                ings['measuer'] = ing['measuer']
                ings['quantity'] = int(ing['quantity']) * person
                dishes_ingredients[name_ing] = ings
            else:
                dishes_ingredients[name_ing]['quantity'] += int(ing['quantity']) * person
    pprint(dishes_ingredients)





get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

#
# portion_counter(['Утка по-пекински', 'Фахитос'], 1)



