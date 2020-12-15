# cloud-events

cloud-events is a python process that runs alongside a postgres database. It listens to events raised by the database (i.e. NOTIFY statements or pg_notify calls), and generate a `cloudevent` in response.

The `cloudevent` conforms to the CNCF [specification](https://cloudevents.io/), and is sent to Amazon SNS. Events are also logged to cloud_events.log. 

Here is an example event:
```json
{"specversion": "1.0", "id": "73569dce-6b1b-4513-9c5e-12e8edee8dfe", "source": "35.233.160.178:5432", "type": "com.trifacta.lightweight", "time": "2020-12-15T02:38:27.545431+00:00", "data": {"id": 1, "to": "vbalasubramaniam@trifacta.com", "subject": "Test Message", "body": "Test Message from Postgres", "created": "2020-12-14T14:25:45.170864+00:00"}}
```