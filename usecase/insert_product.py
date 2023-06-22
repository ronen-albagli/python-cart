from usecase.base import BaseUseCase
from ports.product_mongo_port import ProductMongoPort
from ports.product_stripe_port import StripeProductPort
from typing import Type, TypeVar, TypedDict

ProductMongoPort = TypeVar('ProductMongoPort', bound=ProductMongoPort)
StripeProductPort = TypeVar('StripeProductPort', bound=StripeProductPort)


class UseCaseConfig(TypedDict):
    mongoProduct: Type[ProductMongoPort]
    stripeProduct: Type[StripeProductPort]
    

class CreateProductUseCase(BaseUseCase):
    config: UseCaseConfig
    
    def __init__(self, usecaseConfig: UseCaseConfig):
        self.config = usecaseConfig
        
    def execute(self, product_data):
        stripeResults = self.config.get('stripeProduct').store(product_data=product_data)
        
        product_data['priceId'] = stripeResults.get('priceId')
        product_data['productId'] = stripeResults.get('productId')
        
        self.config.get('mongoProduct').store(product_data=product_data);
        
        return stripeResults
        