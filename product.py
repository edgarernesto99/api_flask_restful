from flask import jsonify, request
from flask_restful import Resource
from model import Product
import json
from model import db

class ProductController(Resource):
    def get(self):
        products = Product.query.all()
        result = [p.to_dict() for p in products]
        return jsonify(result)

    def post(self):
        data = request.get_json()
        print(data)

        product = Product(
            name=data['name'],
            price=data['price'],
            amount=data['amount']
        )
        print(product)

        db.session.add(product)
        db.session.commit()

        return {'status': 'Product added'}

    def put(self):
        data = request.get_json()

        product = Product.query.filter_by(id=data['id']).first()
        if not product:
            return {'status': 'Error - Product does not exist'}
        print(product)
        product.name = data['name']
        product.price = data['price']
        product.amount = data['amount']
        print(product)
        db.session.commit()

        return {'status': 'Product modified'}

    def delete(self):
        id = request.get_json()['id']

        product = Product.query.filter_by(id=id).delete()

        if not product:
            return {'status': 'Error - Product id does not exist'}

        db.session.commit()

        return {'status': 'Product deleted'}