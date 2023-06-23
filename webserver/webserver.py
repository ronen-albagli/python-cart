from webserver.register_routes import register_routes
from flask import Flask

def start_webserver():
    
    print('Startig web server layer')

    app = Flask(__name__)

    register_routes(app)

    app.run(host="0.0.0.0", port=8004, debug=True)