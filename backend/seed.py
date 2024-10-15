from app import app
from models import db, User, Gift, Occasion, Orders

with app.app_context():

    print("Deleting existing data...")
    User.query.delete()
    Gift.query.delete()
    Occasion.query.delete()
    Orders.query.delete()

    print("Creating new data...")
    # Create users
    user1 = User(name='John Doe', email='john@example.com', phone_number=1234567890, password='password')
    user2 = User(name='Jane Smith', email='jane@example.com', phone_number=9876543210, password='password')
    

    # Create occasions
    occasion1 = Occasion(name='Birthday')
    occasion2 = Occasion(name='Anniversary')


    # Create gifts
    gift1 = Gift(name='Gift 1', description='Description 1', price=10.99, image='image1.jpg', occasion=occasion1, creator=user1)
    gift2 = Gift(name='Gift 2', description='Description 2', price=15.99, image='image2.jpg', occasion=occasion2, creator=user2)


    # Create orders
    order1 = Orders(name="Birthday gift", user_id=user1.id, gift_id=gift1.id, quantity=2, price=21.98)
    order2 = Orders(name="Birthday gift",user_id=user2.id, gift_id=gift2.id, quantity=1, price=15.99)

    # Add all objects to the session
    db.session.add_all([user1, user2, occasion1, occasion2, gift1, gift2, order1, order2])
    # Commit the changes to the database
    db.session.commit()
    print("Data creation complete.")