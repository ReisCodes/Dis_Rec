import boto3

s3 = boto3.resource('s3')

s3.create_bucket(Bucket='reis-tech221', CreateBucketConfiguration={
    'LocationConstraint': 'eu-west-1'})

print('Bucket created')

import boto3

s3 = boto3.resource('s3')

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_name="reis-tech221"

s3.Bucket(bucket_name).upload_file('/home/ubuntu/test.txt','test.txt')

print('File Uploaded')

import boto3

s3 = boto3.resource('s3')

s3.Object(bucket_name, 'test.txt').delete()

print('File Deleted')

import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('reis-tech221')
bucket.delete

print('Bucket deleted')

