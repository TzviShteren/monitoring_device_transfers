from flask import Flask, Blueprint

from device_movement_service.app.routes.analysis_routes import analysis_blueprint

app = Flask(__name__)

app.register_blueprint(analysis_blueprint, url_prefix='/api/v1/analysis')

if __name__ == '__main__':
    app.run(port=5002)
