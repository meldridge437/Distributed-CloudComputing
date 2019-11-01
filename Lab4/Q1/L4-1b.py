"""
Lab4: Q1B
-Start and stop Detailed Monitoring of an EC2 instance 
"""

import boto3
import sys

ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
    responce = ec2.monitor_instances(InstanceIds=['i-0cbdfd3b8eb059376'])
else:
    responce = ec2.unmonitor_instances(InstanceIds=['i-0cbdfd3b8eb059376'],)
print(responce)
