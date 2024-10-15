from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User, Gift, Occasion, Orders
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gift galore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)



@app.route('/gifts', methods=['GET'])
def get_gifts():
    gifts = Gift.query.all()
    gift_list = []
    
    for gift in gifts:
        gift_list.append({
            'id': gift.id,
            'name': gift.name,
            'description': gift.description,
            'price': gift.price,
            'occasion_id': gift.occasion_id,
            'user_id': gift.user_id,
            'image': gift.image
        })
    
    return jsonify(gift_list), 200

@app.route('/gifts/<int:id>', methods=['GET'])
def get_gift(id):
    gift = Gift.query.get(id)
    if gift:
        return jsonify({
            'id': gift.id,
            'name': gift.name,
            'description': gift.description,
            'price': gift.price,
            'occasion_id': gift.occasion_id,
            'user_id': gift.user_id,
            'image': gift.image
        }), 200



@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []

    for user in users:
        user_list.append({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone_number': user.phone_number
        })

    return jsonify(user_list), 200


if __name__== '_main_':
    app.run(port=5555, debug=True)