import time
import os

from dotenv import load_dotenv
load_dotenv()


database=os.getenv('DATABASE')
user=os.getenv('DBUSER')
host=os.getenv('HOST')
password=os.getenv('PASSWORD')
port=os.getenv('PORT')


print(database)
print(user)
print(host)
print(password)
print(port)