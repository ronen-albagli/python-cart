from ports.customer_stripe_port import CustomerStripePort
import json

class ProductStripGateway(CustomerStripePort):
    def __init__(self, stripProduct, stripPrices):
        self.stripProduct = stripProduct
        self.stripPrices = stripPrices
        
        
    def store(self, product_data):
        metadata = {
            'credits': str(product_data.get('quota').get('credits')),
            'seats': str(product_data.get('quota').get('seats'))
            
        }
        
        
        product = self.stripProduct.create(
            name=product_data.get('product_name'),
            type=product_data.get('product_type'),
            description=product_data.get('product_description'),
            metadata=metadata
            
        )

        price = product_data.get('product_prices')
    
        priceCreated = self.stripPrices.create(
            product=product.id,
            unit_amount=price['amount'],
            currency=price['currency'],
            metadata=price.get('metadata', None)
        )
        

        result = {
            'productId': priceCreated.product,
            'priceId': priceCreated.id
        }
        
        return result


    
    def modifyStripProduct(self, id, customerEmail):         
        self.stripProduct.modify(
            id,
            email = customerEmail
        )
        
    def appendMetadata(self, product_id, data):  
        product =  self.stripProduct.retrieve(product_id)       
        product.metadata['firstName'] = data.get('firstName')
        product.metadata['lastName'] = data.get('lastName')
        
        product.save();
        
        
        
    
    