import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket="vgomez-boto3-12222024", Key="home/ec2-user/environment/luit-gold-python-repo/test_text_string.txt", Body="Hey, this is a string.", ContentType='text/plain')