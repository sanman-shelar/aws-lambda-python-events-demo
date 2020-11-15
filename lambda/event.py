import os
import boto3
import json

def handler(event, context):

    print('## ENVIRONMENT VARIABLES')
    print(json.dumps(os.environ))
    print('## EVENT')
    print(json.dumps(event))

    return {
        "statusCode": 200
    }