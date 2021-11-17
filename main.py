from pip._vendor import requests
import json

SALADS = 1
SANDWICHES = 2
PIZZAS = 3
DESERTS = 4
DRINKS = 5

def create_lines(data):
    category_id = data['categoryID']
    category_name = data['categoryName']

    for dish in data['dishList']:
        dishId = dish['dishId']
        dish_name = dish['dishName']
        dish_description = dish['dishDescription']
        dish_price = int(dish['dishPrice'])
        new_line = [category_id, category_name, dishId, dish_name, dish_description, dish_price]
        
        print(new_line)


if __name__ == '__main__':

    page = requests.get('https://tenbis-static.azureedge.net/restaurant-menu/19156_en')
    json_data = json.loads(page.text)

    salads = json_data['categoriesList'][SALADS]
    sandwiches = json_data['categoriesList'][SANDWICHES]
    pizzas = json_data['categoriesList'][PIZZAS]
    deserts = json_data['categoriesList'][DESERTS]
    drinks = json_data['categoriesList'][DRINKS]


    create_lines(pizzas)





