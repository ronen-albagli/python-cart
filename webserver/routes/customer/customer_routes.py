from flask import Flask
from flask import Blueprint, request, jsonify
from usecase.insert_subscription import Create_subscription_use_case
from usecase.insert_customer import Create_customer_use_case
from usecase.update_customer_payment import Update_customer_payment
import logging

from app_config.config import get_config
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s', filename='app.log')


def register_customer_routes(app: Flask, router_blueprint):
    @router_blueprint.route('/customer/create', methods=['POST'])
    def insertCustomer():
        config = get_config();
        
        stripeApi = config.get_by_path('STRIPE_SECRET_KEY');
        
        stripeGateway = config.getStripeCustomerGateway()
        mongoCustomerGateway = config.getMongoCustomerGateway()
        # awsGateway = config.getAwsS3LocalGateway()
        
        data = request.json
        
        usecase = Create_customer_use_case({
               'stripeCustomer': stripeGateway,
                'mongoCustomer': mongoCustomerGateway,
                # 'awsGateway': awsGateway
            })
        
        output = usecase.execute(data)
        
        return "New Customer has been inserted"
    
    @router_blueprint.route('/customer/payment', methods=['PATCH'])
    def update_customer_card_details():
        config = get_config()
        data = request.json
                
        stripeGateway = config.getStripeCustomerGateway()
        mongoCustomerGateway = config.getMongoCustomerGateway()
        
        usecase = Update_customer_payment({
               'stripeCustomer': stripeGateway,
                'mongoCustomer': mongoCustomerGateway,
               
        })
        
        usecase.execute(data)
        
        return "Payment updated"
        
        
        
        
        # 'pm_card_visa'
        