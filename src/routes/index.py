from flask import Flask
from flask_cors import CORS
from .get_sales import get_sales_bp
from .get_lstm_sales import get_lstm_sales_bp
from .get_all_products import get_all_products_bp

def create_app():
  app = Flask(__name__)
  CORS(app)
  app.register_blueprint(get_sales_bp)
  app.register_blueprint(get_lstm_sales_bp)
  app.register_blueprint(get_all_products_bp)
  return app

app = create_app()

if __name__ == '__main__':
  app.run(debug=True)
