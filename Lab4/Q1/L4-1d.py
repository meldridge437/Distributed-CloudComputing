"""
Lab4: Q1B
-Reboot an EC2 instance 
"""
import boto3
import sys
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    ec2.reboot_instances(InstanceIds=['i-0cbdfd3b8eb059376'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You do not have permission to reboot instances")
        raise
#Dry Run succeeded, run start_instances again without the Dry Run option
try:
    responce = ec2.reboot_instances(InstanceIds=['i-0cbdfd3b8eb059376'], DryRun=False)
    print("Succes",responce)
except ClientError as e:
    print("Error",e)
