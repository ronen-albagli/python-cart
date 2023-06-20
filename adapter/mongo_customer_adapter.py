from ports.customer_port import CustomerPort

class CustomerMongoGateway(CustomerPort):
    def __init__(self, stripCustomer):
        self.stripCustomer = stripCustomer
        
    def store(self, email, source):
        customer = self.stripCustomer.create()
        
        cust_id =  customer.get('id')
        
        self.stripCustomer.modify(
            cust_id,
            email = email
        )
        
        
    
    