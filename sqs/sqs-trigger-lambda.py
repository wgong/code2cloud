import boto3
from datetime import datetime
import json
import os

_BUCKET_NAME = os.environ.get('MAAS_BUCKET_NAME')
_AWS_KEY_ID = os.environ.get('MAAS_KEY_ID')
_AWS_ACCESS_KEY = os.environ.get('MAAS_ACCESS_KEY')

s3 = boto3.resource('s3', 
      aws_access_key_id=_AWS_ACCESS_KEY_ID, 
      aws_secret_access_key=_AWS_SECRET_ACCESS_KEY
    )
    

def lambda_handler(event, context):
  body = {
      "message": "MaaS SQS data",
      "event": event
  }
  maas_data = json.dumps(body)
  print(maas_data)

  # write to S3
  ts = datetime.utcnow()
  s3object = s3.Object(_BUCKET_NAME, f"{ts}.json")
  s3object.put(
      Body=(bytes(maas_data.encode('UTF-8')))
  )

  response = {
      "statusCode": 200,
      "body": maas_data
  }

  return response
