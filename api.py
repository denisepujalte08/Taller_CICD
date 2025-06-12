import os
from flask import Flask, request, jsonify
from flask_wtf.csrf import CSRFProtect
from main import es_mayor_de_edad

app = Flask(__name__)
# Usar variable de entorno para SECRET_KEY, con fallback solo para desarrollo
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'change-me-in-production')

# Configurar CSRF solo para métodos que lo requieren
app.config['WTF_CSRF_ENABLED'] = True
csrf = CSRFProtect(app)


@app.route("/mayor", methods=["GET"])
@csrf.exempt  # GET requests para APIs públicas no requieren CSRF
def verificar():
    """
    Endpoint para verificar si una persona es mayor de edad.
    Este endpoint es de solo lectura (GET) y no modifica estado,
    por lo que es seguro excluirlo de protección CSRF.
    """
    edad = float(request.args.get("edad", 0))
    resultado = es_mayor_de_edad(edad)
    return jsonify({"mayor_de_edad": resultado})


@app.route("/health", methods=["GET"])
@csrf.exempt  # Health check no requiere CSRF
def health_check():
    """
    Endpoint de health check para monitoreo.
    No procesa datos sensibles ni modifica estado.
    """
    return jsonify({"status": "healthy", "service": "edad-verificador"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
