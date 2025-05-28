from fastapi import HTTPException
from confluent_kafka import Producer
import json

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092'
}

# Kafka producer
producer = Producer(conf)

def send_event(event, topic_name):
    try:
        print(json.dumps(event).encode('utf-8'))
        producer.produce(topic_name, value=json.dumps(event).encode('utf-8'))
        producer.flush()
        print("status: Event sent successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))