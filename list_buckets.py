import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

buckets = response['Buckets']  # will list all the bucket information

for bucket in buckets:
    print(bucket['Name'], bucket['CreationDate']) # Shows us a list of bucket names with their creation dates