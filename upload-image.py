#AKIATUXURLSALNVGOWJ2

#Z8htWK9rjdy36d1ysW6FahKKe+VCuZHK3jCIL6rs

import boto3 
from botocore.client import Config

ACCESS_KEY_ID='AKIATUXURLSALNVGOWJ2'
ACCESS_SECRET_KEY='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'

BUCKET_NAME='imagebucket-121'
FILE_NAME='download.jpg'

data=open(FILE_NAME, 'rb')
s3=boto3.resource(
   's3',
   aws_access_key_id=ACCESS_KEY_ID,
   aws_secret_access_key=ACCESS_SECRET_KEY,
   config=Config(signature_version='s3v4')
)

s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME,Body=data,ACL='public-read')

print("done")