from ports.customer_stripe_port import CustomerStripePort

class CatalogMongoGateway(CustomerStripePort):
    def __init__(self, mongoCatalog):
        self.mongoCatalogCollection = mongoCatalog
        
    def store(self, customerId):
        self.mongoCatalogCollection.insert_one({'customerId': customerId});

        
    
    