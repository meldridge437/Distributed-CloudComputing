"""
Lab4: Download files to an S3 Bucket
"""
import boto3
import botocore
s3 = boto3.resource('s3')
fileName = 'README2.md'
bucketName = 'lab4q2a-bucket'
key = 'README.md'
s3.Bucket(bucketName).download_file(key, fileName)