from api.utils.transbank_config import get_webpay_transaction
from datetime import datetime

class WebpayService:
    def __init__(self):
        self.transaction = get_webpay_transaction()

    # Inicia una transacción de compra con Webpay
    def iniciar_transaccion(self, amount, session_id, return_url):
        buy_order = f"orden-{int(datetime.now().timestamp())}"
        response = self.transaction.create(buy_order, session_id, amount, return_url)
        return response

    # Confirma una transacción de compra con Webpay
    def confirmar_transaccion(self, token_ws):
        return self.transaction.commit(token_ws)
