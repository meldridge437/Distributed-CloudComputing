"""
Lab4: Q1B
-Create new key pairs 
"""
import boto3
ec2 = boto3.client('ec2')
message = ec2.create_key_pair(KeyName="MattLab4-1f-Key")
print("Sucess",message)
