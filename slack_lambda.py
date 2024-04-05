import json
import requests

def lambda_handler(event, context):
    message = {'text': 'server down'}
    url = 'https://hooks.slack.com/services/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'
    try:
        requests.post(url, json=message)
        print("Alert Sent To Slack Successfully..")
    except:
        print("No Alert Sent To Slack..")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }