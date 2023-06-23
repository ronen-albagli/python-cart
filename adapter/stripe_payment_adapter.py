from ports.payment_stripe_port import PaymentStripePort

class PaymentsStripeGateway(PaymentStripePort):
    def __init__(self, stripePayments):
        self.stripePayments = stripePayments
        
    def storeIntent(self, customer_id,invoice_id, product_id, price, default_payment_method_id):
        invoice=invoice_id
        
        paymentIntent =  self.stripePayments.create(
            amount=price,
            currency='usd',
            payment_method_types=['card'],
            customer=customer_id,
          )

        return paymentIntent
    
        
        
    def complete_payment(self, payment_intent_id,payment_method):

        intent = self.stripePayments.retrieve(payment_intent_id)
        
        intent.confirm(
               payment_method=payment_method
        )