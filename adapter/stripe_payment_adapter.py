from ports.payment_stripe_port import PaymentStripePort

class PaymentsStripeGateway(PaymentStripePort):
    def __init__(self, stripePayments):
        self.stripePayments = stripePayments
        
    def storeIntent(self, customer_id, price_id, product_id, price):
        return self.stripePayments.create(
            amount=price,
            currency='usd',
            payment_method_types=['card'],
            customer=customer_id,
            metadata={
                'product_id': product_id
                }   
        )
        
        
    def complete_payment(self, customer,payment_intent_id):
        return  self.stripePayments.confirm(
                    payment_intent_id,
                    # customer,
                    payment_method='pm_1NLqUOIJTenxdmPoEgU2Kjqh'
                )
    