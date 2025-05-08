from flask import Blueprint, request, jsonify
from api.services.product_service import ProductService
from api.services.user_service import UserService
from api.services.currency_service import CurrencyService  # Asegúrate de tener este importado
from datetime import datetime

def register_routes(app, mysql):
    api_bp = Blueprint('api', __name__)
    product_service = ProductService(mysql)
    user_service = UserService(mysql)
    currency_service = CurrencyService()

    @api_bp.route('/products', methods=['GET'])
    def get_products():
        products = product_service.get_all_products()
        return jsonify(products)
    
    @api_bp.route('/users', methods=['GET'])
    def get_users():
        users = user_service.get_all_users()
        return jsonify(users)
    
    
    @api_bp.route('/currency/usd', methods=['GET'])
    def get_dolar():
        data = currency_service.get_dolar_actual()
        return jsonify(data)


    @api_bp.route('/currency/eur', methods=['GET'])
    def get_euro_actual():
        result = currency_service.get_euro_actual()
        return jsonify(result)

    @api_bp.route('/convert/clp-to-usd', methods=['GET'])
    def convert_clp_to_usd():
        try:
            amount = float(request.args.get("amount", 0))
            dolar_info = currency_service.get_dolar_actual()
            if "valor" not in dolar_info:
                return jsonify({"error": "No se pudo obtener la tasa de cambio del dólar"}), 500
            converted = round(amount / dolar_info["valor"], 2)
            return jsonify({
                "clp": amount,
                "usd": converted
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @api_bp.route('/convert/clp-to-eur', methods=['GET'])
    def convert_clp_to_eur():
        try:
            amount = float(request.args.get("amount", 0))
            euro_info = currency_service.get_euro_actual()
            if "valor" not in euro_info:
                return jsonify({"error": "No se pudo obtener la tasa de cambio del euro"}), 500
            converted = round(amount / euro_info["valor"], 2)
            return jsonify({
                "clp": amount,
                "eur": converted
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 400


    app.register_blueprint(api_bp)
