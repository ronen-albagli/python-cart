from flask import Flask
from flask import Blueprint, request, jsonify
from usecase.insert_subscription import Create_subscription_use_case
from app_config.config import get_config

def register_subscription_routes(app: Flask, router_blueprint):
    @router_blueprint.route('/subscription/create', methods=['POST'])
    def create_subscription():
        config = get_config();
        mongoGateway = config.getMongoSubscriptionGateway()
        subscriptionStripeGateway = config.getStripeSubscriptionGateway()
        mongoCustomersGateway = config.getMongoCustomerGateway()
        
        
        data = request.json
        
        usecase = Create_subscription_use_case({
            'stripeSubscription': subscriptionStripeGateway,
            'mongoCustomer': mongoCustomersGateway,
            'mongoSubscription': mongoGateway
        }) 
        
        usecase.execute(data.get('account_id'), data.get('price_id'),data.get('product_id'))
        
        return "Doc has been inserted"
    
    # Register the blueprint with the Flask application