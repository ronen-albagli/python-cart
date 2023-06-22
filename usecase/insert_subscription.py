
from ports.subscription_mongo_port import SubscriptionPort
from ports.subscription_stripe_port import SubscriptionStripePort
from ports.customer_mongo_port import CustomerMongoPort


from typing import Type, TypeVar, TypedDict

SubscriptionPort = TypeVar('SubscriptionPort', bound=SubscriptionPort)
SubscriptionStripePort = TypeVar('SubscriptionStripePort', bound=SubscriptionStripePort)
CustomerMongoPort = TypeVar('CustomerMongoPort', bound=CustomerMongoPort)


# Define the typed dictionary
class UseCaseConfig(TypedDict):
    stripeSubscription: Type[SubscriptionStripePort]
    mongoSubscription: Type[SubscriptionPort]
    mongoCustomer: Type[CustomerMongoPort]

class Create_subscription_use_case():
    config: UseCaseConfig
    def __init__(self, usecaseConfig: UseCaseConfig):
        self.config = usecaseConfig
    
    
    def execute(self, account_id, price_id, product_id):
        customer = self.config['mongoCustomer'].findByAccountId(account_id)
        print("CUSTOMER", customer)
        if customer:
            subscription = self.config.get('stripeSubscription').store(customer['customerId'], price_id,product_id)
            sub_id = subscription.get('id')
            print('SUBSCRIPTION_ID', sub_id)
            self.config.get('mongoSubscription').store(customer['customerId'], product_id, sub_id, 'pending')
            
        else:
            raise ValueError("No customer found for account id: '{account_id}'.")

        
        