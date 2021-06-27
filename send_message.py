import os
import json
from urllib import request, parse, error
from textwrap import wrap

MAX_CHUNK_SIZE = 4096  # Maximum Telegram message length

def lambda_handler(event, context):
    url = 'https://api.telegram.org/bot%s/sendMessage' % os.environ['TOKEN']
    message = event['Records'][0]['Sns']['Message']       #Get the SNS message

    chunks = wrap(message, MAX_CHUNK_SIZE)

    for chunk in chunks:
        data = parse.urlencode({'chat_id': os.environ['CHAT_ID'], 'text': chunk})
        try: 
            request.urlopen(url, data.encode('utf-8'))    #Send the SNS message chunk to Telegram
        except error.HTTPError as e:
            print('Failed to send message:\n%s' % chunk)
            response = json.load(e)
            if 'description' in response:
                print(response['description'])
            raise e
            
