from flask import Flask
from flask import Blueprint, request, jsonify
from webserver.routes.customer.customer_routes import register_customer_routes
from usecase.insert_subscription import Create_subscription_use_case
from usecase.insert_customer import Create_customer_use_case
from app_config.config import get_config

def register_subscription_routes(app: Flask, router_blueprint):
    # Create a blueprint for the routes
    router_blueprint = Blueprint('router', __name__)

    @router_blueprint.route('/subscription/create', methods=['POST'])
    def insert():
        config = get_config();
        mongoGateway = config.getMongoGateway()
        
        usecase = Create_subscription_use_case(mongoGateway)
        
        usecase.execute({"test": 1})
        
        return "Doc has been inserted"
    
    # Register the blueprint with the Flask application