# Add required imports 
from confluent_kafka import Producer 
from config import config 


# Create callback function 
'''
Create a function called callback() that can be passed to the produce() method 
'''

def callback(err, event):
    if err:
        print(f'Produce to topic {event.topic()} failed for event: {event.key()}')
    else:
        val = event.value().decode('utf8')
        print(f'{val} sent to partition {event.partition}.')

# Create function to produce to hello_topic 
'''
Create a function called say_hello() that takes a producer and a key.
'''

'''
producer.produce(topic, [val], [key], [partition], [on_delivery],[timestamp],[headers])
'''
def say_hello(producer, key):
    value = f'Hello {key}!'
    producer.produce('hello_topic', value, key, on_delivery=callback)



if __name__=='__main__':
    producer = Producer(config)
    keys = ['Amy','Breda','Cindy','Derrick','Elaine', 'Fred']
    [say_hello(producer, key) for key in keys]
    producer.flush()