import os

def handler(event, context):

    print('## ENVIRONMENT VARIABLES')
    print(os.environ)
    print('## EVENT')
    print(event)

    return {
        "statusCode": 200
    }