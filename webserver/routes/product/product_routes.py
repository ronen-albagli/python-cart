from flask import Flask
from flask import Blueprint, request, jsonify
from usecase.insert_product import CreateProductUseCase
from app_config.config import get_config

from typing import List, Dict

class StripeProduct:
    def __init__(
        self,
        name: str,
        type: str,
        description: str,
        attributes: List[str] = None,
        metadata: Dict[str, str] = None,
        images: List[str] = None
    ):
        self.name = name
        self.type = type
        self.description = description
        self.attributes = attributes
        self.metadata = metadata
        self.images = images

    def to_dict(self) -> Dict[str, any]:
        product_dict: Dict[str, any] = {
            'name': self.name,
            'type': self.type,
            'description': self.description,
            'attributes': self.attributes,
            'metadata': self.metadata,
            'images': self.images
        }
        return product_dict


def register_product_routes(app: Flask, router_blueprint):
    @router_blueprint.route('/product/create', methods=['POST'])
    def createProduct():
        config = get_config();
        
        stripeGateway = config.getStripeProductGateway()
        mongoProduct = config.getMongoProductGateway()
        
        data = request.json
        
        usecase = CreateProductUseCase({
            'stripeProduct': stripeGateway,
            'mongoProduct': mongoProduct,
            })

                
        output = usecase.execute(data)
        
        print('*******', output);
        
        return "New Customer has been inserted"
        