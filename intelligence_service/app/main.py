from flask import Flask, Blueprint

from intelligence_service.app.routes.intelligence_routes import intelligence_blueprint

app = Flask(__name__)

app.register_blueprint(intelligence_blueprint, url_prefix='/api/v1/intelligence')

if __name__ == '__main__':
    app.run(port=5003)
