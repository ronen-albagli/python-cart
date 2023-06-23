from flask import Flask
from flask import Blueprint, request, jsonify
from usecase.insert_invoice import Create_invoice_use_case
from usecase.complete_payment_intent import Complete_payment_intent_use_case
from app_config.config import get_config

def register_invoice_routes(app: Flask, router_blueprint):
    @router_blueprint.route('/invoice/create', methods=['POST'])
    def create_invoice_intent():
        config = get_config();
        
        stripeGateway = config.getInvoiceStripeGateway()
        mongoInvoice = config.getInvoiceMongoGateway()
        mongoCustomerGateway = config.getMongoCustomerGateway()
        mongoProductGateway = config.getMongoProductGateway()
        
        data = request.json
        
        usecase = Create_invoice_use_case({
               'mongoInvoice': mongoInvoice,
               'mongoCustomer': mongoCustomerGateway,
               'stripeInvoice': stripeGateway,
               'productMongo': mongoProductGateway
            })
        
        
        output = usecase.execute(data['account_id'], data['product_id'])
        
        return output.id, 201

        