from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'  # Corrected from _tablename_ to __tablename__

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    phone_number = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=False)

    gifts = db.relationship('Gift', back_populates='creator', cascade='all, delete-orphan')

    # Serialization rules
    serialize_rules = ('-password', '-gifts.user')

    def __repr__(self):  # Corrected from _repr_ to __repr__
        return f'<User {self.name}>'

class Occasion(db.Model, SerializerMixin):
    __tablename__ = 'occasions'  # Corrected from _tablename_ to __tablename__

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    gifts = db.relationship('Gift', back_populates='occasion')

    # Serialization rules
    serialize_rules = ('-gifts.occasion',)

    def __repr__(self):  # Corrected from _repr_ to __repr__
        return f'<Occasion {self.name}>'

class Gift(db.Model, SerializerMixin):
    __tablename__ = 'gifts'  # Corrected from _tablename_ to __tablename__

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    occasion_id = db.Column(db.Integer, db.ForeignKey('occasions.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    image = db.Column(db.String)

    occasion = db.relationship('Occasion', back_populates='gifts')
    creator = db.relationship('User', back_populates='gifts')

    # Serialization rules
    serialize_rules = ('-occasion.gifts', '-creator.gifts')

    def __repr__(self):  # Corrected from _repr_ to __repr__
        return f'<Gift {self.name}>'

class Orders(db.Model, SerializerMixin):
    __tablename__ = 'orders'  # Corrected from _tablename_ to __tablename__

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    gift_id = db.Column(db.Integer, db.ForeignKey('gifts.id'), nullable=True)
    price = db.Column(db.Integer, nullable=False)

    user = db.relationship('User')
    gift = db.relationship('Gift')

    # Serialization rules
    serialize_rules = ('-user.orders', '-gift.orders')

    def __repr__(self):  # Corrected from _repr_ to __repr__
        return f'<Order {self.name}>'
