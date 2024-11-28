from flask import Flask

from app.routes.phone_routes import phone_blueprint
from app.routes.movements_routes import connected_blueprint
app = Flask(__name__)

app.register_blueprint(phone_blueprint, url_prefix='/api/phone_tracker')
app.register_blueprint(connected_blueprint, url_prefix='/api/connected')

if __name__ == '__main__':
    app.run()
