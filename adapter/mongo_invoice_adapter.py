from ports.invoice_mongo_port import InvoicePort

class InvoiceMongoGateway(InvoicePort):
    def __init__(self, invoiceCollection):
        self.collection = invoiceCollection
        
    def store(self, accountId, customer_id, invoice_id, product_id, price_id,status):
        self.collection.insert_one({'accountId':accountId, 'customer_id':customer_id, 'invoice_id': invoice_id, 'product_id':product_id, 'price_id':price_id, 'status':status})
        
    
    def update_invoice_status(self, invoice_id, status): 
        self. collection.update_one({"invoice_id": invoice_id}, {'$set': {'status': status}})
        
    
    