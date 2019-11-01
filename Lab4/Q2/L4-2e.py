"""
Lab4: Create Presigned URL
"""
import boto3
s3 = boto3.client('s3')
fileName = 'README2.md'
bucketName = 'lab4q2a-bucket'
key = 'README.md'
url = s3.generate_presigned_url(ClientMethod='get_object',Params={
    'Bucket': bucketName,
    'Key': key
})
print(url)