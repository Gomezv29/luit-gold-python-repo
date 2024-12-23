import boto3

s3 = boto3.client('s3')

with open("/home/ec2-user/environment/luit-gold-python-repo/test_text.txt", 'rb') as f:
    s3.put_object(Bucket="vgomez-boto3-12222024", Key="/home/ec2-user/environment/luit-gold-python-repo/test_text.txt", Body=f, ContentType='text/plain')