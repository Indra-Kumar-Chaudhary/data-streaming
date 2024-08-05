# Add Required imports 
from confluent_kafka import Consumer, KafkaException 
from config import config 

# Create function to update configuration 
'''
Create a function called set_consumer_configs(). We will call this method in the main block in order to
add some consumer specific configuration properties.
'''

def set_consumer_configs():
    config['group.id'] = 'hello_group'
    config['auto.offset.reset'] = 'earliest'
    config['enable.auto.commit'] = False 


# Create callback function for partition assignment 
'''
Create a function called assignment_callback() that takes a consumer and a key.
'''
def assignment_callback(consumer, partitions):
    for p in partitions:
        print(f'Assigned to {p.topic}, partion {p.partition}')


'''
This callback will be passed into the consumer.subscribe() call and it will be invoked whenever
topic partition are assigned to this consumer. This includes during the subscribe() call, as well
as any subsequent rebalancing.
'''

if __name__=='__main__':
    set_consumer_configs()
    consumer = Consumer(config)
    consumer.subscribe(['hello_topic'], on_assign=assignment_callback)

    '''
    Here we are updating the config Dictionary, creating our Consumer and then calling the subscribe() method.
    This method takes a list of topic names. This is often a list of one. We are passing a function for the on_assign callback.
    We could also pass in functions for on_revoke and on_lost, but these are less commonly used.
    '''

    # Adding try|except|finally block.
    '''
    We're going to be adding an endless loop in the next step, so we'll use the except KeyboardInterrupt 
    to catch a CTRL-C to stop the program, and then we'll call consumer.close() in the finally block to make 
    sure we clean up after ourselves.
    '''
    try:
        # To add poll loop, and the following while loop between the try: and except.
        while True:
            event = consumer.poll(1.0)
            if event is None:
                continue 
            if event.error():
                raise KafkaException(event.error())
            else:
                val = event.value().decode('utf8')
                partition = event.partition()
                print(f'Received: {val} from partition {partition} ')
                consumer.commit(event)

                '''
                In our loop, we call consumer.poll() repeatedly and then print the value of the event that is received,
                along with the partition that it came from. Notice that the consumer.commit() call is commented for now.
                '''
    except KeyboardInterrupt:
        print('Canceld by user.')
    finally:
        consumer.close()
    

# Run the consumer 
#python consumer.py