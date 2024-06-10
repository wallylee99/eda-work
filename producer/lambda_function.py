import boto3
import json
import datetime

# EventBridge client
eventBridgeClient = boto3.client('events')

def lambda_handler(event, context):

   category = event['category']
   value = event['value']
   location = event['location']

   if not category or not value or not location:
      raise ValueError("Missing one or more required parameters: category, value, location")
   
   # Define the event details
   event_detail = {
      "category": category,
      "value": value,
      "location": location
   }

   # Publish Order Notification event
   response = eventBridgeClient.put_events(
      Entries=[
          {
            'Time': datetime.datetime.utcnow(),
            'Source': 'com.aws.orders',
            'DetailType': 'Order Notification',
            'Detail': json.dumps(event_detail),
            'EventBusName': 'Orders'
          }
      ]
   )

   print(response)

   return {
     'statusCode': 200,
     'body': json.dumps('Event published successfully'),
     'headers': {
        'Content-Type': 'application/json'
     }
   }
    

