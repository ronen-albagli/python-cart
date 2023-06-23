from ports.invoice_mongo_port import InvoicePort
from ports.invoice_stripe_port   import InvoiceStripePort
from ports.payment_stripe_port import PaymentStripePort

from ports.product_mongo_port import ProductMongoPort
from ports.customer_mongo_port import CustomerMongoPort
from typing import Type, TypeVar, TypedDict
from ports.customer_stripe_port import CustomerStripePort

# SubscriptionPort = TypeVar('SubscriptionPort', bound=SubscriptionPort)
InvoiceStripePort = TypeVar('InvoiceStripePort', bound=InvoiceStripePort)
InvoicePort = TypeVar('InvoicePort', bound=InvoicePort)
CustomerMongoPort = TypeVar('CustomerMongoPort', bound=CustomerMongoPort)
PaymentStripePort = TypeVar('PaymentStripePort', bound=PaymentStripePort)
CustomerStripePort = TypeVar('CustomerStripePort', bound=CustomerStripePort)


# Define the typed dictionary
class UseCaseConfig(TypedDict):
    stripeInvoice: Type[InvoiceStripePort]
    mongoInvoice: Type[InvoicePort]
    mongoCustomer: Type[CustomerMongoPort]
    productMongo: Type[ProductMongoPort]
    stripePayment: Type[PaymentStripePort]
    stripeCustomer: Type[CustomerStripePort]
    
class Create_invoice_use_case():
    config: UseCaseConfig
    def __init__(self, usecaseConfig: UseCaseConfig):
        self.config = usecaseConfig
    
    
    def execute(self, account_id, product_id):
        customer = self.config['mongoCustomer'].findByAccountId(account_id)

        if customer:
            product = self.config['productMongo'].get_by_id(product_id)
            
            invoice = self.config.get('stripeInvoice').store(customer['customerId'])
            
            invoice_id = invoice.get('id')
            
            self.config.get('mongoInvoice').store(account_id, customer['customerId'], invoice_id, product_id, product['priceId'],'pending')
                        
            return invoice
            
            
        else:
            raise ValueError("No customer found for account id: '{account_id}'.")

        
        