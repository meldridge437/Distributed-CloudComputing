"""
Lab4: Q1B
-Get security group info 
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    message = ec2.describe_security_groups(GroupIds=['sg-1272e470'])
    print("Sucess",message)
except ClientError as e:
    print(e)
