import time
from faker import Faker
import psycopg2
import random
import os 

from dotenv import load_dotenv
load_dotenv()


database=os.getenv('DATABASE')
user=os.getenv('DBUSER')
host=os.getenv('HOST')
password=os.getenv('PASSWORD')
port=os.getenv('PORT')


conn = psycopg2.connect(database=database, 
                        user=user, 
                        host=host,
                        password=password,
                        port=port)

fake = Faker()
cur = conn.cursor()

# Create tables
def createTables():
    cur.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id SERIAL PRIMARY KEY,
        name TEXT,
        email TEXT,
        address TEXT
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name TEXT,
        price REAL
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        order_date TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
    ''')

# Generate and insert data
def generate_customers(n):
    for _ in range(n):
        name = fake.name()
        email = fake.email()
        address = fake.address()
        cur.execute('INSERT INTO customers (name, email, address) VALUES (%s, %s, %s)', (name, email, address))


def generate_products(n):
    for _ in range(n):
        name = fake.word()
        price = round(random.uniform(10.0, 100.0), 2)
        cur.execute('INSERT INTO products (name, price) VALUES (%s, %s)', (name, price))


if __name__=="__main__":
    # Create tablels 
    cur.execute("ROLLBACK")
    createTables()
    conn.commit()

    # Generate customers
    cur.execute("ROLLBACK")
    generate_customers(100)
    conn.commit()

    # Generate products
    cur.execute("ROLLBACK")
    generate_products(50)
    conn.commit()

    ## Close conn
    conn.close()

