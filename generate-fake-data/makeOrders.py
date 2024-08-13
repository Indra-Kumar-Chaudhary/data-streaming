import time
from faker import Faker
import psycopg2
import random
import os
import logging

database = os.environ['DATABASE']
user=os.environ['USER']
host=os.environ['HOST']
password=os.environ['PASSWORD']
port=os.environ['PORT']

fake = Faker()
conn = psycopg2.connect(database=database, 
                        user=user, 
                        host=host,
                        password=password,
                        port=port)

cur = conn.cursor()

def generate_orders(n):
    #customer_ids = cur.execute('SELECT id FROM customers').fetchall()
    cur.execute('SELECT id FROM customers')
    customer_ids = cur.fetchall()
    cur.execute('SELECT id FROM products')
    product_ids = cur.fetchall()
    #product_ids = cur.execute('SELECT id FROM products').fetchall()

    for _ in range(n):
        # customer_id = random.choice(customer_ids)[0]
        # product_id = random.choice(product_ids)[0]
        customer_id = random.choice(customer_ids)
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 5)
        order_date = fake.date_this_year()
        cur.execute('INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES (%s, %s, %s, %s)', (customer_id, product_id, quantity, order_date))
        logging.warning("New order placed by customer: %s", customer_id)
        logging.warning(time.sleep(5))
        logging.warning("wait for 5 seconds")


if __name__=="__main__":
    cur.execute("ROLLBACK")
    generate_orders(500000)
    conn.commit()
    conn.close()
