"""
Lab4: Retrieve a bucket access control list
"""
import boto3
import json
bucketName = 'lab4q2a-bucket'
s3 = boto3.client('s3')
responce = s3.get_bucket_acl(Bucket=bucketName)
print(responce)