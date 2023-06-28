import os
from pymongo import MongoClient
from dotenv import load_dotenv
from adapter.mongo_subscription_adapter import SubscriptionMongoGateway
from adapter.stripe_subscription_adapter import SubscriptionStripeGateway
from adapter.mongo_customer_adapter import CustomerMongoGateway
from adapter.mongo_product_adapter import ProductMongoGateway
from adapter.stripe_customer_adapter import CustomerStripGateway
from adapter.aws_localstack_adapter import AWSS3LocalStackGateway
from adapter.aws_sqs_adapter import AWSQS3Gateway
from adapter.stripe_product_adapter import ProductStripGateway
from adapter.stripe_payment_adapter import PaymentsStripeGateway
from adapter.stripe_invoice_adapter import InvoiceStripeGateway
from adapter.mongo_invoice_adapter import InvoiceMongoGateway
import boto3

import stripe


class Config():   
    def __init__(self) -> None:
        load_dotenv()
    
    def get_by_path(self, path): 
        return os.getenv(path)
    
    def getMongoClient(self): 
        return MongoClient(self.get_by_path('MONGO_CON_STR'))
    
    def getStripe(self):
         stripe.api_key = self.get_by_path('STRIPE_SECRET_KEY');
         
         return stripe

    def getMongoSubscriptionGateway(self):
        client = self.getMongoClient()
        
        subscription_collection = client.get_database('billing').get_collection('subscriptions')
        
        return SubscriptionMongoGateway(subscription_collection)
    
    def getMongoCustomerGateway(self):
        client = self.getMongoClient()
        
        customer_collection = client.get_database('billing').get_collection('customers')
        
        return CustomerMongoGateway(customer_collection)
    
    def getMongoCustomerGateway(self):
        client = self.getMongoClient()
        
        customers_collection = client.get_database('billing').get_collection('customers')
        
        return CustomerMongoGateway(customers_collection)
    
    def getMongoCatalogGateway(self):
        client = self.getMongoClient()
        
        catalog_collection = client.get_database('billing').get_collection('catalog')
        
        return CustomerMongoGateway(catalog_collection)
    
    def getMongoPlanGateway(self):
        client = self.getMongoClient()
        
        plans_collection = client.get_database('billing').get_collection('plans')
        
        return CustomerMongoGateway(plans_collection)
    
    def getMongoProductGateway(self):
        client = self.getMongoClient()
        
        product_collection = client.get_database('billing').get_collection('products')
        
        return ProductMongoGateway(product_collection)
    
    def getStripeCustomerGateway(self):
        stripe = self.getStripe()
        
        return CustomerStripGateway(stripe.Customer, stripe.PaymentMethod)

    def getStripeProductGateway(self):
        stripe = self.getStripe()
        
        return ProductStripGateway(stripe.Product, stripe.Price)
    
    def getStripeSubscriptionGateway(self):
        stripe = self.getStripe()
        
        return SubscriptionStripeGateway(stripe.Subscription)
    
    def getStripeWebhook(self):
        stripe = self.getStripe()
        
        return stripe.WebhookEndpoint
    
    def getPaymentIntentGateway(self):
        stripe = self.getStripe()
        
        return PaymentsStripeGateway(stripe.PaymentIntent)
    
    def getInvoiceMongoGateway(self):
        client = self.getMongoClient()
        invoice_collection = client.get_database('billing').get_collection('invoice')
        
        return InvoiceMongoGateway(invoice_collection)
        
    def getInvoiceStripeGateway(self):
        stripe = self.getStripe()
        
        return InvoiceStripeGateway(stripe.Invoice,stripe.InvoiceItem)
        
    def getAwsS3LocalGateway(self):
        return AWSS3LocalStackGateway()
    
    def getAwsSQSGateway(self):
        return AWSQS3Gateway(boto3.client(
            'sqs',
            # endpoint_url=aws_host,  # LocalStack S3 endpoint
            aws_access_key_id=self.get_by_path('AWS_ACCESS_KEY'),   # Replace with your AWS Access Key ID
            aws_secret_access_key=self.get_by_path('AWS_SECRET_KEY'),  # Replace with your AWS Secret Access Key
            region_name='us-east-1'  # Replace with your desired AWS region
        ))


appConfig = Config()

def get_config():
    return appConfig
