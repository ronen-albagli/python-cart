import os
from pymongo import MongoClient
from dotenv import load_dotenv
from adapter.mongo_subscription_adapter import SubscriptionMongoGateway
from adapter.stripe_subscription_adapter import SubscriptionStripeGateway
from adapter.mongo_customer_adapter import CustomerMongoGateway
from adapter.mongo_product_adapter import ProductMongoGateway
from adapter.stripe_customer_adapter import CustomerStripGateway
from adapter.aws_localstack_adapter import AWSS3LocalStackGateway
from adapter.stripe_product_adapter import ProductStripGateway
from adapter.stripe_payment_adapter import PaymentsStripeGateway
import stripe


class Config():   
    def __init__(self) -> None:
        load_dotenv()
    
    def get_by_path(self, path): 
        return os.getenv(path)
    
    def getMongoClient(self): 
        #  return MongoClient(self.get_by_path('MONGO_HOST'), int(self.get_by_path('MONGO_PORT')))
        return MongoClient(self.get_by_path('MONGO_CON_STR'))
    
    def getStripe(self):
         print("self.get_by_path('STRIPE_SECRET_KEY');", self.get_by_path('STRIPE_SECRET_KEY'))
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
        
    def getAwsS3LocalGateway(self):
        return AWSS3LocalStackGateway()


appConfig = Config()

def get_config():
    return appConfig
