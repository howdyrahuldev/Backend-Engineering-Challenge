from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    order_id = len(orders) + 1
    orders.append(data)
    return jsonify({'message': 'Order created successfully', 'order_id': order_id}), 201

if __name__ == '__main__':
    app.run(debug=True)