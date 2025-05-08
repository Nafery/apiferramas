import bcchapi
from datetime import datetime, timedelta
import pandas as pd

class CurrencyService:
    def __init__(self, credentials_file="credenciales.txt" ):
        self.api_url = "https://si3.bcentral.cl/SieteRestWS/SieteRestWS"  # Informativo
        self.siete = bcchapi.Siete(file=credentials_file)

    def get_dolar_actual(self):
        try:
            codigo_dolar = "F073.TCO.PRE.Z.D"
            hoy = datetime.today()
            hace_7_dias = hoy - timedelta(days=7)
            desde = hace_7_dias.strftime('%Y-%m-%d')
            hasta = hoy.strftime('%Y-%m-%d')

            df = self.siete.cuadro(
                series=[codigo_dolar],
                nombres=["usd"],
                desde=desde,
                hasta=hasta,
                observado={"usd": "last"}  # último valor disponible
            )

            if not df.empty:
                ultimo_valor = df.iloc[-1]  # última fila
                return {
                    "fecha": str(ultimo_valor.name.date()),
                    "moneda": "USD",
                    "valor": float(ultimo_valor["usd"])
                }
            else:
                return {"error": "No hay datos del dólar en los últimos días."}

        except Exception as e:
            return {"error": f"Error obteniendo dólar: {str(e)}"}



    def get_euro_actual(self):
        try:
            codigo_euro = "F072.CLP.EUR.N.O.D"
            hoy = datetime.today()
            hace_7_dias = hoy - timedelta(days=7)
            desde = hace_7_dias.strftime('%Y-%m-%d')
            hasta = hoy.strftime('%Y-%m-%d')

            df = self.siete.cuadro(
                series=[codigo_euro],
                nombres=["eur"],
                desde=desde,
                hasta=hasta,
                observado={"eur": "last"}  # último valor disponible
            )

            if not df.empty:
                ultimo_valor = df.iloc[-1]  # última fila
                return {
                    "fecha": str(ultimo_valor.name.date()),
                    "moneda": "EUR",
                    "valor": float(ultimo_valor["eur"])
                }
            else:
                return {"error": "No hay datos del euro en los últimos días."}

        except Exception as e:
            return {"error": f"Error obteniendo euro: {str(e)}"}


