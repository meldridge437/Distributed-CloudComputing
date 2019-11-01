"""
Lab4: Upload files to an S3 Bucket
"""
import boto3
s3_client = boto3.client('s3')
fileName = 'README.md'
bucketName = 'lab4q2a-bucket'
s3_client.upload_file(fileName, bucketName, fileName)
