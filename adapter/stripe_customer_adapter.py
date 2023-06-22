from ports.customer_stripe_port import CustomerStripePort

class CustomerStripGateway(CustomerStripePort):
    def __init__(self, stripCustomer, stripPayment):
        self.stripCustomer = stripCustomer
        self.stripPayment = stripPayment
        
    def store(self):
        customer = self.stripCustomer.create()
        
        return customer
    
    def modifyStripCustomer(self, id, customerEmail):         
        self.stripCustomer.modify(
            id,
            email = customerEmail
        )
        
    def appendMetadata(self, customer_id, data):  
        customer =  self.stripCustomer.retrieve(customer_id)       
        customer.metadata['firstName'] = data.get('firstName')
        customer.metadata['lastName'] = data.get('lastName')
        
        customer.save();
        
    def update_customer_card_info(self, customer_id, card_token): 
        payment_method = self.stripPayment.attach(
            card_token,
            customer=customer_id
        )
        
        print('PAYMENT', payment_method)
        
        return self.stripCustomer.modify(
            customer_id,
            invoice_settings={
                'default_payment_method':payment_method.id
            }
        )
        
        
        
    
    