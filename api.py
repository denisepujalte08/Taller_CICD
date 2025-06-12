import os
from flask import Flask, request, jsonify
from main import es_mayor_de_edad

app = Flask(__name__)

# Configuración de la aplicación usando variable de entorno
# En producción, configurar FLASK_SECRET_KEY como variable de entorno
secret_key_name = 'FLASK_SECRET_KEY'
fallback_secret = 'development-key-only'
app.config['SECRET_KEY'] = os.environ.get(secret_key_name, fallback_secret)


@app.route("/mayor", methods=["GET"])
def verificar():
    """
    Endpoint público para verificar si una persona es mayor de edad.

    Parámetros:
        edad (float): Edad a verificar

    Returns:
        JSON: {"mayor_de_edad": boolean}

    Esta es una API de solo lectura que no requiere protección CSRF
    ya que no modifica datos ni estado del servidor.
    """
    try:
        edad_param = request.args.get("edad", "0")
        edad = float(edad_param)
        resultado = es_mayor_de_edad(edad)
        return jsonify({"mayor_de_edad": resultado})
    except (ValueError, TypeError):
        return jsonify({
            "error": "Parámetro 'edad' debe ser un número válido"
        }), 400


@app.route("/health", methods=["GET"])
def health_check():
    """
    Endpoint de verificación del estado del servicio.

    Returns:
        JSON: Estado del servicio
    """
    return jsonify({
        "status": "healthy",
        "service": "edad-verificador",
        "version": "1.0.0"
    })


@app.errorhandler(404)
def not_found(error):
    """Manejo de rutas no encontradas"""
    return jsonify({"error": "Endpoint no encontrado"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Manejo de errores internos del servidor"""
    return jsonify({"error": "Error interno del servidor"}), 500


if __name__ == "__main__":
    # Configuración para desarrollo
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host="0.0.0.0", port=5000, debug=debug_mode) 