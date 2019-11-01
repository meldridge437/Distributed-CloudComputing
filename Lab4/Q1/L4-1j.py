"""
Lab4: Q1B
-Delete security group 
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    message = ec2.delete_security_group(GroupName="TheWizardIsHere")
    print("Sucess",message)
except ClientError as e:
    print(e)
