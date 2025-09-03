from flask import Flask, jsonify, request
from password_generator.generator import PasswordGenerator

app = Flask(__name__)

@app.route("/generate_password", methods=["GET"])
def generate_password():
    length = int(request.args.get("length", 12))
    use_symbols = request.args.get("use_symbols", "true").lower() == "true"
    use_uppercase = request.args.get("use_uppercase", "true").lower() == "true"

    generator = PasswordGenerator(length=length, use_symbols=use_symbols, use_uppercase=use_uppercase)
    password = generator.generate()

    return jsonify({"password": password})

if __name__ == "__main__":
    app.run(debug=True)
