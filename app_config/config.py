import os
from pymongo import MongoClient
from dotenv import load_dotenv
from adapter.mongo_subscription_adapter import SubscriptionMongoGateway
from adapter.mongo_customer_adapter import CustomerMongoGateway
import stripe


class Config():   
    def __init__(self) -> None:
        load_dotenv()
    
    def get_by_path(self, path): 
        return os.getenv(path)
    
    def getMongoClient(self): 
         return MongoClient(self.get_by_path('MONGO_HOST'), int(self.get_by_path('MONGO_PORT')))
    

    def getMongoSubscriptionGateway(self):
        client = self.getMongoClient()
        
        subscription_collection = client.get_database('billing').get_collection('subscriptions')
        
        return SubscriptionMongoGateway(subscription_collection)
    
    def getMongoCustomerGateway(self):
        client = self.getMongoClient()
        
        customer_collection = client.get_database('billing').get_collection('customers')
        
        return SubscriptionMongoGateway(customer_collection)
    
    def getStripeCustomerGateway(self):
        stripe.api_key = self.get_by_path('STRIPE_SECRET_KEY');
        
        return CustomerMongoGateway(stripe.Customer)


appConfig = Config()

def get_config():
    return appConfig
