import boto3

#client = boto3.client('s3') we'll be changing the variable, just in case if we're working with multiple clients, so our code won't be confusing.

s3 = boto3.client('s3')

# to create a bucket
response = s3.create_bucket(
    Bucket ='vgomez-boto3-12222024'
)

print(response) #comes back as a dictionary object