from ports.customer_stripe_port import CustomerStripePort

class PlansMongoGateway(CustomerStripePort):
    def __init__(self, mongoPlans):
        self.mongoPlansCollection = mongoPlans
        
    def store(self, customerId):
        self.mongoPlansCollection.insert_one({'customerId': customerId});

        
    
    