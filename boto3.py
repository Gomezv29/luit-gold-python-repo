import boto3

#s3 = boto3.client('s3', aws_access_key_id="", aws_secret_access_key="", aws_session_token="")


# Main 3 boto3 service interfaces
         # Ways that boto3 communicates with aws
         
# First interface
session = boto3.Session()

# Next one is a low lvl interface that provides direct access to aws using api type methods.
s3 = session.client('s3')

# We can also do the above with 
s3 = boto3.client('s3')
# by pulling up the interface with client we get more control over things we can do with aws

# 3rd interface is the resource interface
s3 = boto3.resource('s3') # High lvl way to pull up an interface and is the more Python way of dealing with aws resource
# can also be called by
s3 = session.resource('s3')

