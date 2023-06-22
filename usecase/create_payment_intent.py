
# from ports.subscription_mongo_port import SubscriptionPort
from ports.payment_stripe_port import PaymentStripePort
from ports.product_mongo_port import ProductMongoPort

from usecase.base import BaseUseCase
from ports.customer_mongo_port import CustomerMongoPort


from typing import Type, TypeVar, TypedDict

# SubscriptionPort = TypeVar('SubscriptionPort', bound=SubscriptionPort)
PaymentStripePort = TypeVar('PaymentStripePort', bound=PaymentStripePort)
ProductMongoPort = TypeVar('ProductMongoPort', bound=ProductMongoPort)
CustomerMongoPort = TypeVar('CustomerMongoPort', bound=CustomerMongoPort)



# Define the typed dictionary
class UseCaseConfig(TypedDict):
    stripePayment: Type[PaymentStripePort]
    mongoProduct: Type[ProductMongoPort]
    mongoCustomer: Type[CustomerMongoPort]
    
class Create_payment_intent_use_case(BaseUseCase):
    config: UseCaseConfig
    def __init__(self, usecaseConfig: UseCaseConfig) -> None:
        self.config = usecaseConfig
        
    def execute(self, account_id, product_id):
        customer = self.config['mongoCustomer'].findByAccountId(account_id)
        product = self.config['mongoProduct'].get_by_id(product_id)
        
        price = product['product_prices']['amount']
        
        print('%%%%product', price)
        
        if customer:
            paymentIntent = self.config['stripePayment'].storeIntent(customer['customerId'], product['priceId'],product_id, price)
            paymentId = paymentIntent.get('id')
            print('PAYMENT_ID', paymentId)
            # self.config.get('mongoSubscription').store(customer['customerId'], product_id, sub_id, 'pending')
            
        else:
            raise ValueError("No customer found for account id: '{account_id}'.")

        
