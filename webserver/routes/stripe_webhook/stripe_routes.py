from flask import Flask
from flask import Blueprint, request, jsonify

from app_config.config import get_config

def register_stripe_routes(app: Flask, router_blueprint):
    @router_blueprint.route('/stripe/webhook/payment-intent', methods=['POST'])
    def insertPaymentIntentWebhook():
        config = get_config();
        
        stripeWebhook = config.getStripeWebhook()
        # awsGateway = config.getAwsS3LocalGateway()
        webhook_endpoint = stripeWebhook.create(
            url='https://92ae-2a10-8012-15-394-45cf-b5ac-fe63-dbe7.eu.ngrok.io/stripe/webhook/income/payment-intent',
            enabled_events=["payment_intent.succeeded"]
        )
        
        return webhook_endpoint

    @router_blueprint.route('/stripe/webhook/income/payment-intent', methods=['POST'])
    def handlePaymentIntentWebhook():
        config = get_config();
        secret='whsec_i45h0dJdxE0aSOkI8fmLQpj0YtnEJ8N9'
        
        
        stripe = config.getStripe()
        payload = request.get_data(as_text=True)
        sig_header = request.headers.get("Stripe-Signature")
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, secret
            )
            # Handle the event and perform desired actions based on event data
            if event["type"] == "payment_intent.succeeded":
                payment_intent = event["data"]["object"]
                # Perform actions for a successful payment

            return "", 200
        except stripe.error.SignatureVerificationError as e:
            return str(e), 400
            return webhook_endpoint
            