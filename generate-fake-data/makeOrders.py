import time
from faker import Faker
import psycopg2
import random
import os
import logging
import time
import os
import datetime

from dotenv import load_dotenv
load_dotenv()


database=os.getenv('DATABASE')
user=os.getenv('DBUSER')
host=os.getenv('HOST')
password=os.getenv('PASSWORD')
port=os.getenv('PORT')


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
        customer_id = random.choice(customer_ids)[0]
        product_id = random.choice(product_ids)[0]
        quantity = random.randint(1, 5)
        order_date = fake.date_this_year()
        status = "Pending Confirmation"
        cur.execute('INSERT INTO orders (customer_id, product_id, quantity, order_date,status) VALUES (%s, %s, %s, %s, %s)', (customer_id, product_id, quantity, datetime.datetime.now(), status))
        time.sleep(random.randint(1,5))
        logging.warning("New order placed by customer: %s", customer_id)



if __name__=="__main__":
    cur.execute("ROLLBACK")
    generate_orders(500000)
    conn.commit()
    conn.close()
