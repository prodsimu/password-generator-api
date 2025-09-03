from flask import Flask, jsonify, request
from password_generator.generator import PasswordGenerator

app = Flask(__name__)

@app.route('/generate_password', methods=['GET'])
def generate_password_api():
    length = request.args.get('length', default=12, type=int)
    generator = PasswordGenerator(length)
    password = generator.generate()
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)
