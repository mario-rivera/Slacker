from __future__ import print_function

import requests
import json

print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    data = json.loads(event['body'])
    #print( "Received event data: " + json.dumps(data, indent=2) )


    final_url = 'https://hooks.slack.com/services/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'
    payload = {'text': data['slack']}
    response = requests.post(final_url, data=json.dumps(payload))

    response = {
        'statusCode': response.status_code,
        'headers' : {
            "Content-type" : "text/plain"
        },
        'body' : response.text
    };

    # new comment line
    return response
