from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    results = []
    for p in pizzas:
        results.append({
            'id': p.id,
            'name': p.name,
            'ingredients': p.ingredients
        })
    return jsonify(results)
