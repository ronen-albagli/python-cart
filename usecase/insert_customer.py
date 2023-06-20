
from ports.customer_stripe_port import CustomerStripePort
from ports.customer_mongo_port import CustomerMongoPort
from typing import Type

CustomerStripePort = Type[CustomerStripePort]  # Replace with the actual type for CustomerStripePort
CustomerMongoPort = Type[CustomerMongoPort]  # Replace with the actual type for CustomerMongoPort

# Declare the dictionary
UseCaseConfig = {
    'stripeCustomer': CustomerStripePort,
    'mongoCustomer': CustomerMongoPort
}

class Create_customer_use_case():
    config: UseCaseConfig
    def __init__(self, usecaseConfig: UseCaseConfig):
        self.config = usecaseConfig
    
    
    def execute(self, customerData):
        newCustomer =  self.config['stripeCustomer'].store()
        cust_id = newCustomer.get('id');
        
        newCustomer =  self.config['stripeCustomer'].modifyStripCustomer(cust_id, customerData.get('email'))
        
        self.config['stripeCustomer'].appendMetadata(cust_id, customerData);
        
        
        self.config['mongoCustomer'].store(cust_id)