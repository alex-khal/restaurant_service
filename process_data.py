import psycopg2
from pip._vendor import requests
import json
from config import config

SALADS = 1
SANDWICHES = 2
PIZZAS = 3
DESERTS = 4
DRINKS = 5

def create_lines(data):
    category_id = data['categoryID']
    category_name = data['categoryName']
    all_db_lines = []

    for dish in data['dishList']:
        dishId = dish['dishId']
        dish_name = dish['dishName']
        dish_description = dish['dishDescription']
        dish_price = int(dish['dishPrice'])
        new_line = [category_id, category_name, dishId, dish_name, dish_description, dish_price]
        all_db_lines.append(new_line)

    add_line_to_DB(all_db_lines)


def add_line_to_DB(lines):
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.executemany(
        "INSERT INTO dishes(category_id, category_name, dish_id, dish_name, dish_description, dish_price) "
        "VALUES (%s,%s,%s,%s,%s,%s)", lines)
    conn.commit()
    cur.close()
    conn.close()


def load_data(url):
    page = requests.get(url)
    json_data = json.loads(page.text)
    all_data = [
        json_data['categoriesList'][SALADS],
        json_data['categoriesList'][SANDWICHES],
        json_data['categoriesList'][PIZZAS],
        json_data['categoriesList'][DESERTS],
        json_data['categoriesList'][DRINKS]
    ]
    for category in all_data:
        create_lines(category)
