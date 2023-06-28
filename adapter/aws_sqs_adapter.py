from ports.aws_sqs_port import AWSSQSPort
import boto3
import botocore

class AWSQS3Gateway(AWSSQSPort): 
    def __init__(self, client)  -> None:
        self.sqs_client = client
        
    def create_queue(self, queue_name):
        response = self.sqs_client.create_queue(
            QueueName=queue_name + '.fifo',
            Attributes={
                'FifoQueue': 'true',
                'ContentBasedDeduplication': 'true'
            }
         )
            
        return response['QueueUrl']
    
    def publish(self, queue_url, message, account_id):
       response =  self.sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=message,
            MessageGroupId = queue_url
        )
       
       return response['MessageId']
        
        
   