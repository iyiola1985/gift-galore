from app import app, db
from models import User, Occasion, Gift, Order

def seed_data():
    print("Deleting existing data...")
    db.session.query(Order).delete()
    db.session.query(Gift).delete()
    db.session.query(Occasion).delete()
    db.session.query(User).delete()
    db.session.commit()

    print("Creating new data...")
    
    # Create users
    user1 = User(name='John Doe', email='john@example.com', phone_number='1234567890', password='password123')
    user2 = User(name='Jane Smith', email='jane@example.com', phone_number='9876543210', password='password456')
    db.session.add_all([user1, user2])
    db.session.commit()

    # Create occasions
    occasion1 = Occasion(name='Birthday')
    occasion2 = Occasion(name='Anniversary')
    db.session.add_all([occasion1, occasion2])
    db.session.commit()

    # Create gifts
    gift1 = Gift(name='Watch', description='Luxury wristwatch', price=199, occasion=occasion1, creator=user1, image='watch.jpg')
    gift2 = Gift(name='Necklace', description='Diamond necklace', price=299, occasion=occasion2, creator=user2, image='necklace.jpg')
    db.session.add_all([gift1, gift2])
    db.session.commit()

    # Create orders
    order1 = Order(name='Birthday Gift', quantity=1, user=user1, gift=gift1, price=199)
    order2 = Order(name='Anniversary Gift', quantity=1, user=user2, gift=gift2, price=299)
    db.session.add_all([order1, order2])
    db.session.commit()

    print("Seed data created successfully!")

if __name__ == '__main__':
    with app.app_context():
        seed_data()