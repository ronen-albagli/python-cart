
class InvoiceStripePort:
    def store(self, customer_id):
        """Store mongo data implementation come here"""
        pass
    
    def get_by_id(self, in_id):
        pass
    
    def modify_payment(self, id, payment_intent_id):
        pass
    
    def modify_payment_completed(self, invoice_id):
        pass
    
    