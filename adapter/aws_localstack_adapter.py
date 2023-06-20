from ports.aws_s3_port import AWSS3Port
import boto3
import botocore

class AWSS3LocalStackGateway(AWSS3Port): 
    def __init__(self) -> None:
        self.s3_client = boto3.client(
            's3',
            endpoint_url='http://localhost:4566',  # LocalStack S3 endpoint
            aws_access_key_id='YOUR_ACCESS_KEY',   # Replace with your AWS Access Key ID
            aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',  # Replace with your AWS Secret Access Key
            region_name='us-east-1'  # Replace with your desired AWS region
        )
        
    def create_bucket(self, bucket_name):
        bucket = self.s3_client.create_bucket(Bucket=bucket_name)
        
        print('Bucket created')
        
        return bucket
    
    def add_file_to_bucket(self, bucket_name, file_path, name):
        try:
            with open(file_path, 'rb') as file:
                self.s3_client.upload_fileobj(file, bucket_name, name) 
                print("File uploaded successfully.")
                return True
        except botocore.exceptions.ClientError as e:
            print("An error occurred:", e.response['Error']['Message'])
    
    def get_file_bucket(self, bucket_name, file_key, location):
        try:
            self.s3_client.download_file(bucket_name, file_key, location)
            print("File downloaded successfully.")
        except botocore.exceptions.ClientError as e:
            print("An error occurred:", e.response['Error']['Message'])
