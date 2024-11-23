from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import json

import products_dao
import orders_dao
import uom_dao
import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=conn_str_params['user'],
    dbpass=conn_str_params['password'],
    dbhost=conn_str_params['host'],
    dbname=conn_str_params['dbname']
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)
conn = get_sql_connection()


def create_tables():
    cursor = conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE products (
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            uom_id INT NOT NULL,
            price_per_unit DOUBLE PRECISION NOT NULL
        );

        CREATE TABLE uom (
            uom_id SERIAL PRIMARY KEY,
            uom_name VARCHAR(45) NOT NULL
        );

        CREATE TABLE orders (
            order_id SERIAL PRIMARY KEY,
            customer_name VARCHAR(100) NOT NULL,
            total DOUBLE PRECISION NOT NULL,
            datetime TIMESTAMP NOT NULL
        );

        CREATE TABLE order_details (
            order_id INT NOT NULL,
            product_id INT NOT NULL,
            quantity DOUBLE PRECISION NOT NULL,
            total_price DOUBLE PRECISION NOT NULL,
            PRIMARY KEY (order_id, product_id)
        );
        """)
        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
