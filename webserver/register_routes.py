from flask import Flask
from flask import Blueprint, request, jsonify
from usecase.insert_subscription import Create_subscription_use_case
from usecase.insert_customer import Create_customer_use_case
from app_config.config import get_config

def register_routes(app: Flask):
    # Create a blueprint for the routes
    router_blueprint = Blueprint('router', __name__)

    @router_blueprint.route('/subscription/create', methods=['POST'])
    def insert():
        config = get_config();
        mongoGateway = config.getMongoGateway()
        
        usecase = Create_subscription_use_case(mongoGateway)
        
        usecase.execute({"test": 1})
        
        return "Doc has been inserted"
    
    @router_blueprint.route('/customer/create', methods=['POST'])
    def insertCustomer():
        config = get_config();
        stripeGateway = config.getStripeCustomerGateway()
        
        print('stripeGateway',stripeGateway)
        
        data = request.json
        email = data.get('email')
        source=data.get('source')
        
        usecase = Create_customer_use_case(stripeGateway)
        
        output = usecase.execute({"email": email, "source": source})
        
        print('!!!!!', output)
        
        return "New Customer has been inserted"
        

    # Register the blueprint with the Flask application
    app.register_blueprint(router_blueprint)