from flask import Flask, request, jsonify
from flask_wtf.csrf import CSRFProtect
from main import es_mayor_de_edad

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
csrf = CSRFProtect(app)


@app.route("/mayor", methods=["GET"])
@csrf.exempt  # Para APIs GET públicas, excluimos CSRF
def verificar():
    edad = float(request.args.get("edad", 0))
    resultado = es_mayor_de_edad(edad)
    return jsonify({"mayor_de_edad": resultado})


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "service": "edad-verificador"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
