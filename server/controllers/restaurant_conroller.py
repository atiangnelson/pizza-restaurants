from flask import Blueprint, jsonify, abort
from server.app import db
from server.models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    results = []
    for r in restaurants:
        results.append({
            'id': r.id,
            'name': r.name,
            'address': r.address
        })
    return jsonify(results)

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify({'error': 'Restaurant not found'}), 404

    pizzas = []
    for rp in r.restaurant_pizzas:
        pizzas.append({
            'id': rp.pizza.id,
            'name': rp.pizza.name,
            'ingredients': rp.pizza.ingredients,
            'price': rp.price
        })

    return jsonify({
        'id': r.id,
        'name': r.name,
        'address': r.address,
        'pizzas': pizzas
    })

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify({'error': 'Restaurant not found'}), 404

    db.session.delete(r)
    db.session.commit()
    return '', 204
