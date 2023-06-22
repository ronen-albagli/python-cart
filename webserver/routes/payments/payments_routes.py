from flask import Flask
from flask import Blueprint, request, jsonify
from usecase.create_payment_intent import Create_payment_intent_use_case
from usecase.complete_payment_intent import Complete_payment_intent_use_case
from app_config.config import get_config

def register_payment_routes(app: Flask, router_blueprint):
    @router_blueprint.route('/payment/intent/create', methods=['POST'])
    def create_payment_intent():
        config = get_config();
        
        stripeGateway = config.getPaymentIntentGateway()
        mongoCustomerGateway = config.getMongoCustomerGateway()
        productGateway = config.getMongoProductGateway()
        # awsGateway = config.getAwsS3LocalGateway()
        
        data = request.json
        
        usecase = Create_payment_intent_use_case({
               'stripePayment': stripeGateway,
               'mongoCustomer': mongoCustomerGateway,
                'mongoProduct': productGateway
            })
        
        print('mongoCustomerGateway',mongoCustomerGateway)
        
        output = usecase.execute(data['account_id'], data['product_id'])
        
        return "New Customer has been inserted"
        
    @router_blueprint.route('/payment/intent/completed', methods=['POST'])
    def complete_payment_intent():
        config = get_config();
        data = request.json
        
        stripeGateway = config.getPaymentIntentGateway()
        mongoCustomerGateway = config.getMongoCustomerGateway()
        
        
        usecase = Complete_payment_intent_use_case({
               'stripePayment': stripeGateway,
               'mongoCustomer': mongoCustomerGateway,
               
        })
        
        usecase.execute(data['account_id'],data['payment_id'])
        
        return "payment completed"
        
        