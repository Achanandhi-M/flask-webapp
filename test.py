from flask import Flask, request, session, jsonify
from flask_session import Session
import base64

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def calculate_bill(name, presentunit, previousunit):
    total_unit = presentunit - previousunit
    total_amount = total_unit * 10
    return total_unit, total_amount

@app.route('/', methods=['POST'])
def login():
    auth = request.headers.get('Authorization')
    if auth:
        auth_type, auth_credentials = auth.split(' ', 1)
        if auth_type.lower() == 'basic':
            username_password = base64.b64decode(auth_credentials).decode('utf-8')
            username, password = username_password.split(':', 1)
            if username in ['John', 'Bob', 'Jack']:
                session['username'] = username
                return jsonify({"message": "Success", "user": username}), 200
    return jsonify({"message": "User Not Found :("}), 404

@app.route('/bill', methods=['POST'])
def bill():
    auth = request.headers.get('Authorization')
    if auth:
        auth_type, auth_credentials = auth.split(' ', 1)
        if auth_type.lower() == 'basic':
            username_password = base64.b64decode(auth_credentials).decode('utf-8')
            username, password = username_password.split(':', 1)
            if username in ['John', 'Bob','Jack']:
                data = request.get_json()
                presentunit = data.get("Present")
                previousunit = data.get("Previous")
                total_unit, total_amount = calculate_bill(username, presentunit, previousunit)
                return jsonify({
                    "message": "Success",
                    "user": username,
                    "total_units_consumed": total_unit,
                    "total_amount_rupees": total_amount
                }), 200
    return jsonify({"message": "Error"}), 400

if __name__ == '__main__':
    app.run(debug=True)