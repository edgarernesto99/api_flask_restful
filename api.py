from flask import Flask, jsonify, redirect, request
from flask_restful import Api, Resource
from config import config
from model import db
from product import ProductController

def createApp(env):
    app = Flask(__name__)
    app.config.from_object(env)

    # Inicializar db con app flask
    with app.app_context():
        db.init_app(app)
        # db.create_all()

    return app


env = config['development']
app = createApp(env)
api = Api(app)


class Hello(Resource):
    def get(self, name):
        return "Hello"+name

@app.route('/')
def home():
    return "<h1>Hello world</h1>"

api.add_resource(Hello, '/hello/<name>')
api.add_resource(ProductController, '/product')

if __name__ == "__main__":
    app.run()
