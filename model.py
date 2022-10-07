from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class Product(db.Model):
    __tablename__ = 'product'

    id:int = db.Column(db.Integer, primary_key=True, nullable=False)
    name:str = db.Column(db.String(128), nullable=False)
    price:float = db.Column(db.Numeric(5,2), nullable=False)
    amount:int = db.Column(db.Integer, nullable=False)

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def __repr__(self):
        return f'<Product({self.name})>'

    def __str__(self):
        return f'{self.name}'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'amount': self.amount
        }
