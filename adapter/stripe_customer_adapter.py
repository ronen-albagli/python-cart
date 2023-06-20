from ports.customer_stripe_port import CustomerStripePort

class CustomerStripGateway(CustomerStripePort):
    def __init__(self, stripCustomer):
        self.stripCustomer = stripCustomer
        
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
        
        
        
    
    