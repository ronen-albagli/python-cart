
from ports.customer_stripe_port import CustomerStripePort
from ports.customer_mongo_port import CustomerMongoPort
from typing import Type, TypeVar, TypedDict



CustomerStripePort = TypeVar('CustomerStripePort', bound=CustomerStripePort)
CustomerMongoPort = TypeVar('CustomerMongoPort', bound=CustomerMongoPort)

# Define the typed dictionary
class UseCaseConfig(TypedDict):
    stripeCustomer: Type[CustomerStripePort]
    mongoCustomer: Type[CustomerMongoPort]

class Create_customer_use_case():
    config: UseCaseConfig
    def __init__(self, usecaseConfig: UseCaseConfig):
        self.config = usecaseConfig
    
    
    def execute(self, customerData):
        newCustomer =  self.config['stripeCustomer'].store()
        cust_id = newCustomer.get('id');
        accountId = customerData.get('accountId')
        
        newCustomer =  self.config.get('stripeCustomer').modifyStripCustomer(cust_id, customerData.get('email'))
        
        self.config['stripeCustomer'].appendMetadata(cust_id, customerData);
        
        self.config['mongoCustomer'].store(cust_id,accountId)
                        
        return