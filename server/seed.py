from server.models import db
from server.app import app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Pizza Hut", address="YaYa Center")
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")

    db.session.add_all([r1, p1])
    db.session.commit()

    rp = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    db.session.add(rp)
    db.session.commit()


