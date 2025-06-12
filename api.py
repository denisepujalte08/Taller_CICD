from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/mayor", methods=["GET"])
def verificar():
    edad = int(request.args.get("edad", 0))
    resultado = edad >= 18
    return jsonify({"mayor_de_edad": resultado})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
