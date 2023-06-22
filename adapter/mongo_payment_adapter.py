from ports.payment_mongo_port import PaymentPort

class SubscriptionStripeGateway(PaymentPort):
    def __init__(self, stripePayments):
        self.stripePayments = stripePayments
        
    def store(self, customer_id, price_id, product_id):
        return self.stripePayments.create(
            customer=customer_id,
            items=[{
                'price': price_id
            }],
        )
        
        
    
    