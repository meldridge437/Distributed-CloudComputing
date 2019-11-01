"""
Lab4: Retrieve a bucket policy
"""
import boto3
import json
bucketName = 'lab4q2a-bucket'
bucketPolicy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': "arn:aws:s3:::%s/*" % bucketName
    }]
}
fileName = 'README2.md'

bucket_policy = json.dumps(bucketPolicy)
s3 = boto3.client('s3')
s3.put_bucket_policy(Bucket=bucketName,Policy=bucket_policy)
responce = s3.get_bucket_policy(Bucket=bucketName)
print(responce['Policy'])