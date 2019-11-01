"""
Lab4: Create an S3 Bucket
"""
import boto3
s3_client = boto3.client('s3')
responce = s3_client.list_buckets()
#outputsthe bucket names
print('Existing buckets: ')
for bucket in responce['Buckets']:
    print(f' {bucket["Name"]}')