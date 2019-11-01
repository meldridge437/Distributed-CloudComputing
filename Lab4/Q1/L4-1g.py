"""
Lab4: Q1B
-Delete key pair
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    message = ec2.delete_key_pair(KeyName="MattLab4-1f-Key")
    print("Sucess",message)
except ClientError as e:
    print(e)
