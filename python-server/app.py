from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

#ruta de prueba
@app.route('/ping')
def ping():
	return jsonify({ 'mensaje': 'pong' })

# ------------------------------------------- #

@app.route('/products')
def getProducts():
	return jsonify({
		"products": products,
		"message": "products list"
	})

# ------------------------------------------ #

@app.route('/products/<string:productName>')
def getProduct( productName ):
	
	for product in products:

		if productName == product['name']:
			return jsonify({
				"product": product,
				"message": "Producto encontrado"
			})
		
	return jsonify({
		"message": "No se encontro producto"	
	})

# -------------------------------------------- #

@app.route('/products', methods = ['POST'])
def addProduct():
	
	newProduct = {
		'name': request.json['name'],
		'price': request.json['price'],
		'quantity': request.json['quantity']
	}

	products.append( newProduct )

	return jsonify({
		'message': 'nuevo producto agregado exitosamente',
		'products': products
	})

# -------------------------------------------------------- #

@app.route('/products/<string:productName>', methods = ['PUT'])
def updateProduct( productName ):
	
	if len( products ) > 0:

		for product in products:
			if product['name'] == productName:
				product['name'] = request.json['name']
				product['price'] = request.json['price']
				product['quantity'] = request.json['quantity']

				return jsonify({
					'message': 'producto actualizado',
					'products': products
				})

		# sino encuentra producto
		return jsonify({ 'message': 'producto no encontrado' })

	# sino hay productos registrados
	return jsonify({ 'message': 'no hay productos registrados' })

# ---------------------------------------------------------------- #

@app.route('/products/<string:productName>', methods = ['DELETE'])
def deleteProduct( productName ):
	
	if len( products ) > 0:

		for product in products:
			
			if product['name'] == productName:
				products.remove( product )

				return jsonify({
					'message': 'producto actualizado',
					'products': products
				})

		# sino encuentra producto
		return jsonify({ 'message': 'producto no encontrado' })

	# sino encuentra productos registrados
	return jsonify({ 'message': 'no hay productos registrados' })

# -----------------------------------------------------------------  #

if ( __name__ == '__main__' ):
	 app.run( debug = True, port = 4000 )
