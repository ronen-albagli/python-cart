from ports.subscription_mongo_port import SubscriptionPort

class SubscriptionStripeGateway(SubscriptionPort):
    def __init__(self, stripSubscription):
        self.stripSubscription = stripSubscription
        
    def store(self, customer_id, price_id, product_id):
        return self.stripSubscription.create(
            customer=customer_id,
            items=[{
                'price': price_id
            }],
        )
        
        
    
    