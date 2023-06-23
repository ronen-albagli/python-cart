
# from ports.subscription_mongo_port import SubscriptionPort
from ports.payment_stripe_port import PaymentStripePort
from ports.product_mongo_port import ProductMongoPort
from ports.customer_mongo_port import CustomerMongoPort
from ports.customer_stripe_port import CustomerStripePort
from ports.invoice_stripe_port   import InvoiceStripePort
from ports.invoice_mongo_port   import InvoicePort

from usecase.base import BaseUseCase


from typing import Type, TypeVar, TypedDict

# SubscriptionPort = TypeVar('SubscriptionPort', bound=SubscriptionPort)
PaymentStripePort = TypeVar('PaymentStripePort', bound=PaymentStripePort)
ProductMongoPort = TypeVar('ProductMongoPort', bound=ProductMongoPort)
CustomerMongoPort = TypeVar('CustomerMongoPort', bound=CustomerMongoPort)
CustomerStripePort = TypeVar('CustomerStripePort', bound=CustomerStripePort)
InvoiceStripePort = TypeVar('InvoiceStripePort', bound=InvoiceStripePort)
InvoicePort = TypeVar('InvoicePort', bound=InvoicePort)



# Define the typed dictionary
class UseCaseConfig(TypedDict):
    stripePayment: Type[PaymentStripePort]
    mongoProduct: Type[ProductMongoPort]
    mongoCustomer: Type[CustomerMongoPort]
    stripeCustomer: Type[CustomerStripePort]
    stripeInvoice: Type[InvoiceStripePort]
    mongoInvoice: Type[InvoicePort]
    
    
    
class Create_payment_intent_use_case(BaseUseCase):
    config: UseCaseConfig
    def __init__(self, usecaseConfig: UseCaseConfig) -> None:
        self.config = usecaseConfig
        
    def execute(self, account_id, product_id, invoice_id):
        customer = self.config['mongoCustomer'].findByAccountId(account_id)
        product = self.config['mongoProduct'].get_by_id(product_id)
        
        price = product['product_prices']['amount']
        
        stripeCustomer = self.config['stripeCustomer'].retrieve(customer.get('customerId'))
        default_payment_method_id = stripeCustomer.invoice_settings.default_payment_method

        if customer:
            paymentIntent = self.config['stripePayment'].storeIntent(customer['customerId'], invoice_id, product_id, price, default_payment_method_id)
            paymentId = paymentIntent.get('id')
            
            self.config['stripeInvoice'].modify_payment(invoice_id, paymentId)
            
            self.config['stripePayment'].complete_payment(paymentId, default_payment_method_id)
            self.config['stripeInvoice'].modify_payment_completed(invoice_id)
            
            self.config['mongoInvoice'].update_invoice_status(invoice_id,'fulfilled')
            
            return paymentId            
        else:
            raise ValueError("No customer found for account id: '{account_id}'.")

        
