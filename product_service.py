from flask import Flask, request, jsonify

app = Flask(__name__)

products = {}

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product_id = data['id']
    product_name = data['name']
    if product_id in products:
        return jsonify({'message': 'Product already exists'}), 400
    products[product_id] = product_name
    return jsonify({'message': 'Product created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
