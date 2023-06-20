from ports.customer_stripe_port import CustomerStripePort

class CustomerMongoGateway(CustomerStripePort):
    def __init__(self, mongoCustomer):
        self.mongoCustomerCollection = mongoCustomer
        
    def store(self, customerId):
        self.mongoCustomerCollection.insert_one({'customerId': customerId});

        
    
    