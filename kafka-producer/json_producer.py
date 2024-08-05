# Add required imports 

from confluent_kafka import Producer 
from confluent_kafka.serialization import SerializationContext, MessageField 
from confluent_kafka.schema_registry import SchemaRegistryClient 
from confluent_kafka.schema_registry.json_schema import JSONSerializer
from config import config, sr_config 
import time


# Define our class and schema 

 # Add schema_str declaration 
schema_str = """{
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "Temperature",
            "description": "Temperature sensor reading",
            "type": "object",
            "properties": {
            "city": {
                "description": "City name",
                "type": "string"
            },
            "reading": {
                "description": "Current temperature reading",
                "type": "number"
            },
            "unit": {
                "description": "Temperature unit (C/F)",
                "type": "string"
            },
            "timestamp": {
                "description": "Time of reading in ms since epoch",
                "type": "number"
            }
            }
        }"""

data = [Temperature('London', 12, 'C', round(time.time()*1000)),
            Temperature('Chicago', 63, 'F', round(time.time()*1000)),
            Temperature('Berlin', 14, 'C', round(time.time()*1000)),
            Temperature('Madrid', 18, 'C', round(time.time()*1000)),
            Temperature('Phoenix', 78, 'F', round(time.time()*1000))]
'''
Add the following class declaration
'''

class Temperature(object):
    def __init__(self, city, reading, unit, timestamp):
        self.city = city 
        self.reading = reading 
        self.unit = unit 
        self.timestamp = timestamp 
    
   
    
    # Add this function to convert our Temperature object to a dictionary 
    def temp_to_dict(temp, ctx):
        return {"city": temp.city,
                "reading": temp.reading,
                "unit":temp.unit,
                "timestamp":temp.timestamp}

    # CREATE some test data 
    '''
    Add the following list of dictionaries containing some sample temperature readings.
    '''

   
    
    # Create a producer callback function 
    '''
    Add a function to pass in the produce() call to see if it is successful.
    '''

    def delivery_report(err, event):
        if err is not None:
            print(f'Delivery failed on reading for {event.key().decode("utf8")}: {err}')
        else:
            print(f'Temp reading for {event.key().decode("utf8")} produced to {event.topic()}')
    


# Add main block 
if __name__=='__main__':
    topic = 'temp_readings'
    schema_registry_client = SchemaRegistryClient(sr_config)

    json_serializer = JSONSerializer(schema_str,
                                        schema_registry_client,
                                        temp_to_dict)
        
    producer = Producer(config) 

    for temp in data:
        producer.produce(topic=topic, key=str(temp.city),
                        value=json_serializer(temp,
                        SerializationContext(topic, MessageField.VALUE)),
                        on_delivery=delivery_report)
    producer.flush()
   