import flask
import pandas as pd
from config import config
import psycopg2
from flask import request

dishes_service = flask.Flask(__name__)
dishes_service.config["DEBUG"] = True
params = config()
conn = psycopg2.connect(**params)
cur = conn.cursor()


@dishes_service.route('/', methods=['GET'])
def welcome():
    return "Welcome to my menu dishes service app :)"


@dishes_service.route('/drinks', methods=['GET'])
def get_all_drinks():
    df = pd.read_sql("""SELECT dish_id, dish_name, dish_description,dish_price FROM dishes WHERE category_id=279257""",
                     conn)
    return df.to_json(indent=4, date_format='iso', orient='records')


@dishes_service.route('/drink/<id>', methods=['GET'])
def get_certain_drink(id):
    query = """SELECT dish_id, dish_name, dish_description,dish_price FROM dishes WHERE category_id=279257 and dish_id="""
    query += id
    df = pd.read_sql(query, conn)
    return df.to_json(indent=4, date_format='iso', orient='records')


@dishes_service.route('/pizzas', methods=['GET'])
def get_all_pizzas():
    df = pd.read_sql("""SELECT dish_id, dish_name, dish_description,dish_price FROM dishes WHERE category_id=279255""",
                     conn)
    return df.to_json(indent=4, date_format='iso', orient='records')


@dishes_service.route('/pizza/<id>', methods=['GET'])
def get_certain_pizza(id):
    query = """SELECT dish_id, dish_name, dish_description,dish_price FROM dishes WHERE category_id=279255 and dish_id="""
    query += id
    df = pd.read_sql(query, conn)
    return df.to_json(indent=4, date_format='iso', orient='records')


@dishes_service.route('/desserts', methods=['GET'])
def get_all_desserts():
    df = pd.read_sql("""SELECT dish_id, dish_name, dish_description,dish_price FROM dishes WHERE category_id=279256""",
                     conn)
    return df.to_json(indent=4, date_format='iso', orient='records')


@dishes_service.route('/dessert/<id>', methods=['GET'])
def get_certain_dessert(id):
    query = """SELECT dish_id, dish_name, dish_description,dish_price FROM dishes WHERE category_id=279256 and dish_id="""
    query += id
    df = pd.read_sql(query, conn)
    return df.to_json(indent=4, date_format='iso', orient='records')

#TODO - not finished
@dishes_service.route('/order', methods=['POST'])
def get_certain_dessert():

    query = """SELECT SUM(dish_price) FROM dishes WHERE dish_id="""
    df = pd.read_sql(query, conn)
    return df.to_json(indent=4, date_format='iso', orient='records')

#TODO - not finished
@dishes_service.route('drinks_ids, desserts_ids, pizzas_ids', methods=['Body'])
def get_order_body(drinks_ids, desserts_ids, pizzas_ids):
    new_order = {"drinks": drinks_ids, "desserts": desserts_ids, "pizzas": pizzas_ids}
    return new_order


if __name__ == '__main__':
    dishes_service.run()
