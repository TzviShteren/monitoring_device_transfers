from flask import Flask, Blueprint

from analysis_service.app.routes.movements_routes import movements_blueprint

app = Flask(__name__)

app.register_blueprint(movements_blueprint, url_prefix='/api/v1/movements')

if __name__ == '__main__':
    app.run(port=5001)
