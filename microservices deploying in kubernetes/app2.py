from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/orders/<int:user_id>')
def get_orders(user_id):
    user_info_response = requests.get(f'http://user-service:5001/users/{user_id}')
    if user_info_response.status_code == 200:
        user_info = user_info_response.json()
        # For demonstration, assuming orders are hardcoded
        orders = {"orders": ["Order 1", "Order 2"]}
        orders.update(user_info)
        return jsonify(orders)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5002)
