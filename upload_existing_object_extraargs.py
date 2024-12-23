import boto3

s3 = boto3.client('s3')

s3.upload_file('/home/ec2-user/environment/luit-gold-python-repo/test_text.txt', 'vgomez-boto3-12222024', 'test_text.txt', ExtraArgs={'ContentType':'text/plain'})