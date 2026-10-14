import json
import boto3
import os
import uuid
from datetime import datetime, timezone

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

TABLE_NAME = os.environ.get('TABLE_NAME', 'SmartParkingSlots')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')


def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)

    for record in event.get('Records', []):
        body = json.loads(record['body'])

        plate_number = body.get('plate_number', 'UNKNOWN')
        driver_email = body.get('driver_email', 'driver@example.com')
        slot_id = f"SLOT-{uuid.uuid4().hex[:4].upper()}"
        timestamp = datetime.now(timezone.utc).isoformat()

        table.put_item(Item={
            'plate_number': plate_number,
            'slot_id': slot_id,
            'entry_time': timestamp,
            'status': 'OCCUPIED',
            'driver_email': driver_email
        })

        print(f"Allocated {slot_id} to vehicle {plate_number}")

        if SNS_TOPIC_ARN:
            message = (
                f"Smart Parking Confirmation\n"
                f"Vehicle Number: {plate_number}\n"
                f"Assigned Slot: {slot_id}\n"
                f"Entry Time: {timestamp}\n"
                f"Status: Confirmed"
            )

            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject=f"Parking Space Assigned - {slot_id}",
                Message=message
            )

    return {
        "statusCode": 200,
        "body": "Processed successfully"
    }
