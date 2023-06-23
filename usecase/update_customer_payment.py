
from ports.customer_stripe_port import CustomerStripePort
from typing import Type, TypeVar, TypedDict
from ports.customer_mongo_port import CustomerMongoPort


CustomerStripePort = TypeVar('CustomerStripePort', bound=CustomerStripePort)
CustomerMongoPort = TypeVar('CustomerMongoPort', bound=CustomerMongoPort)

# Define the typed dictionary
class UseCaseConfig(TypedDict):
    stripeCustomer: Type[CustomerStripePort]
    mongoCustomer: Type[CustomerMongoPort]

class Update_customer_payment():
    config: UseCaseConfig
    def __init__(self, usecaseConfig: UseCaseConfig):
        self.config = usecaseConfig
    
    
    def execute(self, paymentData):
        customer = self.config['mongoCustomer'].findByAccountId(paymentData['account_id'])

        if customer:
            cust_id = customer.get('customerId')
            card_token = paymentData.get('card_token');

            self.config.get('stripeCustomer').update_customer_card_info(cust_id,card_token)
        else:
            raise ValueError("No customer found for account id: '{account_id}'.")

                      
        return