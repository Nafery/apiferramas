from flask import Blueprint, request, jsonify, redirect
from api.services.product_service import ProductService
from api.services.user_service import UserService
from api.services.currency_service import CurrencyService
from api.services.webpay_service import WebpayService

def register_routes(app, mysql):
    # Define blueprint
    api_bp = Blueprint('api', __name__)
    
    # Instanciar servicios
    product_service = ProductService(mysql)
    user_service = UserService(mysql)
    currency_service = CurrencyService()
    webpay_service = WebpayService()

    # Rutas
    @api_bp.route('/products', methods=['GET'])
    def get_products():
        return jsonify(product_service.get_all_products())
    
    @api_bp.route('/users', methods=['GET'])
    def get_users():
        return jsonify(user_service.get_all_users())
    
    @api_bp.route('/currency/usd', methods=['GET'])
    def get_dolar():
        return jsonify(currency_service.get_dolar_actual())

    @api_bp.route('/currency/eur', methods=['GET'])
    def get_euro_actual():
        return jsonify(currency_service.get_euro_actual())

    @api_bp.route('/convert/clp-to-usd', methods=['GET'])
    def convert_clp_to_usd():
        try:
            amount = float(request.args.get("amount", 0))
            dolar_info = currency_service.get_dolar_actual()
            if "valor" not in dolar_info:
                return jsonify({"error": "No se pudo obtener la tasa de cambio del dólar"}), 500
            converted = round(amount / dolar_info["valor"], 2)
            return jsonify({"clp": amount, "usd": converted})
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
            return jsonify({"clp": amount, "eur": converted})
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        
    @api_bp.route('/webpay/init', methods=['POST'])
    def iniciar_pago():
        data = request.get_json()
        amount = data.get("amount", 1000)
        session_id = data.get("session_id", "usuario_demo")
        return_url = data.get("return_url", "http://127.0.0.1:5000/webpay/confirmar")
        try:
            resp = webpay_service.iniciar_transaccion(amount, session_id, return_url)
            return jsonify({"url": resp["url"], "token": resp["token"]})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @api_bp.route('/webpay/confirmar', methods=['GET', 'POST'])
    def confirmar_pago():
        token_ws = request.args.get("token_ws") or request.form.get("token_ws")
        if not token_ws:
            # Redirige al frontend en caso de error por falta de token
            return redirect("http://localhost:3000/webpay/error")

        try:
            resultado = webpay_service.confirmar_transaccion(token_ws)
            status = resultado.get("status")
            amount = resultado.get("amount")
            buy_order = resultado.get("buy_order")

            if status == "AUTHORIZED":
                # Redirige a la web app con datos por query string
                return redirect(f"http://localhost:3000/webpay/success?amount={amount}&orden={buy_order}")
            else:
                # Redirige a página de fallo de pago
                return redirect("http://localhost:3000/webpay/failed")
        except Exception as e:
            # Redirige a error general si algo falla en el proceso
            return redirect("http://localhost:3000/webpay/error")
        
    @api_bp.route('/webpay/create', methods=['POST'])
    def crear_transaccion_webpay():
        data = request.get_json()
        amount = data.get("amount")
        session_id = data.get("session_id", "default-session")
        return_url = "http://localhost:3000/webpay/response"

        if not amount:
            return jsonify({"error": "El monto es obligatorio"}), 400

        try:
            response = webpay_service.iniciar_transaccion(amount, session_id, return_url)
            return jsonify({"url": response['url'], "token": response['token']})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @api_bp.route('/webpay/confirm', methods=['POST'])
    def confirmar_transaccion_webpay():
        token_ws = request.form.get("token_ws")
        if not token_ws:
            return jsonify({"error": "token_ws no encontrado"}), 400
        try:
            result = webpay_service.confirmar_transaccion(token_ws)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # ✅ Registro del blueprint con prefijo explícito "/"
    app.register_blueprint(api_bp, url_prefix="/")

    # Mostrar rutas registradas
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.rule}")
