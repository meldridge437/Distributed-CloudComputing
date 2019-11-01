"""
Lab4: Q1B
-Get info about key pairs 
"""
import boto3
import sys
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
message = ec2.describe_key_pairs()
print("Sucess",message)
