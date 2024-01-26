import json
import math

def lambda_handler(event, context):
  print('Received event: ' + json.dumps(event, indent=2))

  api_path = event['apiPath']
  http_mehtod = event['httpMethod']
  request_body = event['requestBody']
  props = request_body['content']['application/json']['properties']

  number = ''
  for prop in props:
    if prop['name'] == 'number':
      number = prop['value']
      break
  
  if api_path == '/is_prime':
    if http_mehtod == 'POST':
      output = is_prime(number)   # for external call, here mock up

      response_body ={
        'application/json': {
            'body': json.dumps({'isPrime': output})
        }
      }

      action_response = {
        'actionGroup': event['actionGroup'],
        'apiPath': event['apiPath'],
        'httpMehtod': event['httpMehtod'],
        'httpStatusCode': 200,
        'responseBody': response_body
      }

      session_attributes = event['sessionAttributes']
      prompt_session_attributes = event['promptSessionAttributes']

      api_response = {
        'messageVersion': "1.0",
        'response': action_response,
        'sessionAttributes': session_attributes,
        'promptSessionAttributes': prompt_session_attributes
      }

      return api_response
    else:
      return {
        "statusCode": 500,
        "body": json.dumps({
          "text": "Method not allowed"
        }),
      }
    
def is_prime(n):
    n = int(n)

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True