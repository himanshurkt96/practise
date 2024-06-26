#AKIATUXURLSAC7CB5FMQ
#6rS+EqgArc4UWJE3lEgAduedCqwl3D0ksj6nHfNB

import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='learning-python',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'  
    }
)

print(response)

