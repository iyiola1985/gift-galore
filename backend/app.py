from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User, Gift, Occasion, Order
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gift galore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def home():
    return "Welcome to Gift"

@app.route('/gifts', methods=['GET'])
def get_gifts():
    gifts = Gift.query.all()
    gift_list = [gift.to_dict() for gift in gifts]  # Use to_dict method
    return jsonify(gift_list), 200

@app.route('/gifts/<int:id>', methods=['GET'])
def get_gift(id):
    gift = Gift.query.get(id)
    if gift:
        return jsonify(gift.to_dict()), 200  # Use to_dict method
    return jsonify({'error': 'Gift not found'}), 404



if __name__== '__main__':
    app.run(port=5555, debug=True)