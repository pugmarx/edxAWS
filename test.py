import boto3

s3client = boto3.resource('s3')
s3client.meta.client.upload_file('someFile')