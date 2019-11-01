"""
Lab4: Q1B
-Start and stop Detailed an EC2 instance 
"""

import boto3
import sys
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
action = sys.argv[1].upper()
if action == 'ON':
    try:
        ec2.start_instances(InstanceIds=['i-0cbdfd3b8eb059376'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    #Dry Run succeeded, run start_instances again without the Dry Run option
    try:
        responce = ec2.start_instances(InstanceIds=['i-0cbdfd3b8eb059376'], DryRun=False)
        print(responce)
    except ClientError as e:
        print(e)
else:
    try:
        ec2.stop_instances(InstanceIds=['i-0cbdfd3b8eb059376'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    #Dry Run succeeded, run start_instances again without the Dry Run option
    try:
        responce = ec2.stop_instances(InstanceIds=['i-0cbdfd3b8eb059376'], DryRun=False)
        print(responce)
    except ClientError as e:
        print(e)