from flask import Flask
from flask import Blueprint, request, jsonify
from usecase.insert_subscription import Create_subscription_use_case
from usecase.insert_customer import Create_customer_use_case
from app_config.config import get_config

def register_catalog_routes(app: Flask, router_blueprint):
    @router_blueprint.route('/customer/create', methods=['POST'])
    def createPlan():
        config = get_config();
        
        stripeGateway = config.getStripeCustomerGateway()
        mongoCustomerGateway = config.getMongoCustomerGateway()
        awsGateway = config.getAwsS3LocalGateway()
        
        data = request.json
        
        usecase = Create_customer_use_case({
               'stripeCustomer': stripeGateway,
                'mongoCustomer': mongoCustomerGateway,
                'awsGateway': awsGateway
            })
        
        output = usecase.execute(data)
        
        return "New Customer has been inserted"
        