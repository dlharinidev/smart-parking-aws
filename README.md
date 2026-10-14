# Smart Parking System Using AWS

## Project Overview
A serverless parking workflow that processes vehicle entry
messages, assigns a parking slot, stores vehicle details,
and sends a confirmation email.

## AWS Services
- Amazon SQS: Receives vehicle entry messages
- AWS Lambda: Processes vehicle messages and assigns a slot
- Amazon DynamoDB: Stores vehicle and parking details
- Amazon SNS: Sends parking confirmation emails
- Amazon CloudWatch: Stores execution logs

## Workflow
1. A vehicle entry message enters the SQS queue.
2. SQS triggers the Lambda function.
3. Lambda generates a parking slot ID.
4. Vehicle details are stored in DynamoDB.
5. SNS sends a confirmation email.
6. CloudWatch records execution logs.

## Test Result
- Vehicle: KA-01-AB-1234
- Assigned slot: SLOT-AABF
- Status: OCCUPIED

## Limitation
This demonstration generates random slot IDs. It does not
yet check actual parking capacity or prevent duplicate
slot assignments.

## Technologies
Python, AWS Lambda, Amazon SQS, Amazon DynamoDB,
Amazon SNS, Amazon CloudWatch, Git, and GitHub.
