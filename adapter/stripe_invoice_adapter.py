from ports.invoice_stripe_port import InvoiceStripePort

class InvoiceStripeGateway(InvoiceStripePort):
    def __init__(self, stripeInvoice, invoiceItem):
        self.stripeInvoice = stripeInvoice
        self.invoiceItem = invoiceItem
        
    def get_by_id(self, invoice_id):
        return self.stripeInvoice.retrieve(invoice_id)
    
    def modify_payment(self, invoice_id, payment_intent_id):
        self.stripeInvoice.modify(
       invoice_id,
        metadata={
            'payment_intent': payment_intent_id
        }
    )
    
    def modify_payment_completed(self, invoice_id):
        self.stripeInvoice.modify(
            invoice_id,
            paid=True
            )
        
        
    
    def store(self, customer_id):
        
        invoice =  self.stripeInvoice.create(
            customer=customer_id,
            auto_advance=True,
            collection_method='send_invoice',
            days_until_due=10,

        )
        
        
        return invoice
        
        
    
    