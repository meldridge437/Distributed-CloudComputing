"""
Lab4: Q1B
-Create new security group 
"""
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    message = ec2.create_security_group(GroupName="TheWizardIsHere",Description="Only level 20 wizards allowed")
    print("Sucess",message)
except ClientError as e:
    print(e)
