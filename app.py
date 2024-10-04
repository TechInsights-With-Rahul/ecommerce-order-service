from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Health check endpoint for liveness probe
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Health check endpoint for readiness probe
@app.route('/ready', methods=['GET'])
def ready_check():
    return jsonify({"status": "ready"}), 200

# Simulated in-memory order storage
orders = []

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = {
        "id": len(orders) + 1,
        "user_id": data['user_id'],
        "product_id": data['product_id'],
        "quantity": data['quantity'],
        "total_price": data['total_price']
    }
    orders.append(new_order)
    return jsonify({"message": "Order created", "order": new_order}), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

