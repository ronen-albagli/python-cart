from ports.customer_stripe_port import CustomerStripePort

class CustomerStripGateway(CustomerStripePort):
    def __init__(self, stripCustomer, stripPayment):
        self.stripCustomer = stripCustomer
        self.stripPayment = stripPayment
        
    def store(self):
        customer = self.stripCustomer.create()
        
        return customer
    
    def retrieve(self, customer_id):
        return self.stripCustomer.retrieve(customer_id)
    
    def modifyStripCustomer(self, id, customerEmail, accountId):         
        self.stripCustomer.modify(
            id,
            email = customerEmail,
            metadata= {
                'accountId':accountId
            }
        )
        
    def appendMetadata(self, customer_id, data):  
        customer =  self.stripCustomer.retrieve(customer_id)       
        customer.metadata['firstName'] = data.get('firstName')
        customer.metadata['lastName'] = data.get('lastName')
        customer.metadata['accountId'] = data.get('accountId')
        
        customer.save();
        
    def update_customer_card_info(self, customer_id, card_token): 
        payment_method = self.stripPayment.attach(
            card_token,
            customer=customer_id
        )
        
        return self.stripCustomer.modify(
            customer_id,
            invoice_settings={
                'default_payment_method':payment_method.id
            }
        )
        
        
        
    
    