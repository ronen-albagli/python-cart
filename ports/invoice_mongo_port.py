
class InvoicePort:
    def store(self, stipeInvoiceId, customer_id, product_id, price_id):
        """Store mongo data implementation come here"""
        pass
    
    def getInvoiceById(self, stipeInvoiceId):
        """Get all account subscriptions"""
        pass
    
    def update_invoice_status(self, invoice_id, status):
        pass
    
    