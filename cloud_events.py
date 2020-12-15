#!/usr/bin/python3
import logging
logging.basicConfig(filename='cloud_events.log', format='%(message)s', level=logging.INFO)

import pgpubsub, mysecrets
pubsub = pgpubsub.connect(host='35.233.160.178', user='trifacta', database='main', password=mysecrets.DB_PASSWORD)
from cloudevents.http import CloudEvent, to_binary, to_structured
import requests, json
attributes = {
    "type": "com.trifacta.lightweight",
    "source": "35.233.160.178:5432",
}
import boto3
sns = boto3.client('sns', region_name='us-west-2', aws_access_key_id=mysecrets.KEY, aws_secret_access_key=mysecrets.SECRET)

pubsub.listen('cloud_events')
for e in pubsub.events():
    event = CloudEvent(attributes, data=json.loads(e.payload))
    headers, body = to_structured(event)
    logging.info(body.decode())
    sns.publish(TopicArn='arn:aws:sns:us-west-2:163305015547:cloud_events', Message=str(body))
