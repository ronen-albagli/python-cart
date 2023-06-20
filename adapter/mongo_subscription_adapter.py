from ports.subscription_port import SubscriptionPort

class SubscriptionMongoGateway(SubscriptionPort):
    def __init__(self, subscriptionCollection):
        self.collection = subscriptionCollection
        
    def store(self, subscription_data):
        self.collection.insert_one(subscription_data)
        
        
    
    