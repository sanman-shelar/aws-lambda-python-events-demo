import os
import boto3
import json

def handler(event, context):

    print('## ENVIRONMENT VARIABLES')
    print(os.environ)
    print('## EVENT')
    print(json.dumps(event))

    sns = boto3.client('sns')
    sns.publish(TopicArn=os.environ['PERSON_SNS_TOPIC_ARN'], Message=event['body'])

    return {
        "statusCode": 202
    }