from ports.subscription_mongo_port import SubscriptionPort

class SubscriptionMongoGateway(SubscriptionPort):
    def __init__(self, subscriptionCollection):
        self.collection = subscriptionCollection
        
    def store(self, customer_id, product_id, subscription_id, status):
        print('{customer_id, product_id, subscription_id, status}',{customer_id, product_id, subscription_id, status})
        self.collection.insert_one({'customer_id':customer_id, 'product_id':product_id, 'subscription_id':subscription_id, 'status':status})
        
        
    
    