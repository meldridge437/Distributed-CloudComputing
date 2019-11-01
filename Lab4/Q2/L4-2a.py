"""
Lab4: Create an S3 Bucket
"""
import boto3
import logging
from botocore.exceptions import ClientError
s3 = boto3.client('s3')

def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3')
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
    
create_bucket('lab4q2a-bucket','us-east-2')