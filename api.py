from flask import Flask, request, jsonify
from main import es_mayor_de_edad

app = Flask(__name__)


@app.route("/mayor", methods=["GET"])
def verificar():
    edad = float(request.args.get("edad", 0))
    resultado = es_mayor_de_edad(edad)
    return jsonify({"mayor_de_edad": resultado})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
