
# from ports.subscription_mongo_port import SubscriptionPort
from ports.payment_stripe_port import PaymentStripePort
from ports.product_mongo_port import ProductMongoPort
from ports.customer_stripe_port import CustomerStripePort

from usecase.base import BaseUseCase
from ports.customer_mongo_port import CustomerMongoPort


from typing import Type, TypeVar, TypedDict

# SubscriptionPort = TypeVar('SubscriptionPort', bound=SubscriptionPort)
PaymentStripePort = TypeVar('PaymentStripePort', bound=PaymentStripePort)
CustomerMongoPort = TypeVar('CustomerMongoPort', bound=CustomerMongoPort)
CustomerStripePort = TypeVar('CustomerStripePort', bound=CustomerStripePort)


# Define the typed dictionary
class UseCaseConfig(TypedDict):
    stripePayment: Type[PaymentStripePort]
    mongoCustomer: Type[CustomerMongoPort]
    stripeCustomer: Type[CustomerStripePort]
    
    
class Complete_payment_intent_use_case(BaseUseCase):
    config: UseCaseConfig
    def __init__(self, usecaseConfig: UseCaseConfig) -> None:
        self.config = usecaseConfig
        
    def execute(self, account_id, payment_intent_id):
            customer = self.config['mongoCustomer'].findByAccountId(account_id)
            
            stripeCustomer = self.config['stripeCustomer'].retrieve(customer.get('customerId'))
            default_payment_method_id = stripeCustomer.invoice_settings.default_payment_method

            paymentIntent = self.config['stripePayment'].complete_payment(default_payment_method_id,payment_intent_id)
            paymentId = paymentIntent.get('id')
            
            return paymentId
        
