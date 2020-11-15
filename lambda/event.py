import json
import os
import boto3

def handler(event, context):

    print('## ENVIRONMENT VARIABLES')
    print(os.environ)
    print('## EVENT')
    print(event)

    return {
        "statusCode": 200,
        "body": json.dumps('Response from lambda')
    }