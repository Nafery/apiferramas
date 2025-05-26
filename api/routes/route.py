from flask import Blueprint, request, jsonify, redirect
from api.services.product_service import ProductService
from api.services.user_service import UserService
from api.services.currency_service import CurrencyService
from api.services.webpay_service import WebpayService
from api.services.category_services import CategoryService

def register_routes(app, mysql):
    # Define blueprint
    api_bp = Blueprint('api', __name__)
    
    # Instanciar servicios
    product_service = ProductService(mysql)
    user_service = UserService(mysql)
    currency_service = CurrencyService()
    webpay_service = WebpayService()
    category_service = CategoryService(mysql)

    # Rutas
    @api_bp.route('/products', methods=['GET'])
    def get_products():
        return jsonify(product_service.get_all_products())
    
    @api_bp.route('/products/category/<int:category_id>', methods=['GET'])
    def get_products_by_category(category_id):
        try:
            products = product_service.get_products_by_category(category_id)
            return jsonify(products), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @api_bp.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        
        if not email or not password:
            return jsonify({"error": "Falta un campo"}), 400
        
        user = user_service.get_user_by_credentials(email, password)
        if user:
            return jsonify(user)
        else:
            return jsonify({"error": "Credenciales inválidas"}), 401
        
    @api_bp.route('/categories', methods=['GET'])
    def get_categories():
        try:
            categories = category_service.get_all_categories()
            return jsonify(categories), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @api_bp.route('/users', methods=['GET'])
    def get_users():
        return jsonify(user_service.get_all_users())
    
    @api_bp.route('/currency/usd', methods=['GET'])
    def get_dolar():
        return jsonify(currency_service.get_dolar_actual())

    @api_bp.route('/currency/eur', methods=['GET'])
    def get_euro_actual():
        return jsonify(currency_service.get_euro_actual())

    @api_bp.route('/currency/convert', methods=['POST'])
    def convertir_monedas():
        data = request.get_json()
        try:
            amount = float(data.get("amount", 0))
            conversion = currency_service.convertir_desde_clp(amount)
            return jsonify(conversion)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        
    @api_bp.route('/webpay/init', methods=['POST'])
    def iniciar_pago():
        data = request.get_json()
        amount = data.get("amount", 1000)
        session_id = data.get("session_id", "usuario_demo")
        return_url = "http://localhost:5001/webpay/confirmar"
        try:
            resp = webpay_service.iniciar_transaccion(amount, session_id, return_url)
            return jsonify({"url": resp["url"], "token": resp["token"]})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @api_bp.route('/webpay/confirmar', methods=['GET', 'POST'])
    def confirmar_pago():
        token_ws = request.args.get("token_ws") or request.form.get("token_ws")
        if not token_ws:
            return redirect("http://localhost:5173/webpay/error")
        try:
            resultado = webpay_service.confirmar_transaccion(token_ws)
            status = resultado.get("status")
            amount = resultado.get("amount")
            buy_order = resultado.get("buy_order")

            if status == "AUTHORIZED":
                # 🔧 Redirige al frontend con los datos en la URL
                return redirect(f"http://localhost:5173/webpay/confirmar?amount={amount}&orden={buy_order}&status={status}")
            else:
                return redirect("http://localhost:5173/webpay/failed")
        except Exception as e:
            return redirect("http://localhost:5173/webpay/error")



    # ✅ Registro del blueprint con prefijo explícito "/"
    app.register_blueprint(api_bp, url_prefix="/")

    # Mostrar rutas registradas
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.rule}")
