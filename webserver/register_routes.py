from flask import Flask
from flask import Blueprint
from webserver.routes.customer.customer_routes import register_customer_routes
from webserver.routes.subscription.subscription_routes import register_subscription_routes
from webserver.routes.product.product_routes import register_product_routes
from app_config.config import get_config

def register_routes(app: Flask):
    # Create a blueprint for the routes
    router_blueprint = Blueprint('router', __name__)
    
    register_customer_routes(app, router_blueprint)
    register_product_routes(app, router_blueprint)
    register_subscription_routes(app, router_blueprint)
    
    # Register the blueprint with the Flask application
    app.register_blueprint(router_blueprint)