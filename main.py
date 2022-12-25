from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import app, db
from models import User, Offer, Order


@app.route('/users/', method=['GET'])
def get_all_users():
    try:
        users = db.session.query(User).all()
        return jsonify([user.to_dict() for user in users])
    except Exception as e:
        return f'{e}'


@app.route('/users/<int:id>', method=['GET'])
def get_user_by_id(id):
    try:
        user = db.session.query(User).filter(User.id == id).first()
        return jsonify(user.to_dict())
    except Exception as e:
        return f'{e}'


@app.route('/orders/', method=['GET'])
def get_all_orders():
    try:
        orders = db.session.query(Order).all()
        return jsonify([order.get_order() for order in orders])
    except Exception as e:
        return f'{e}'


@app.route('/orders/<int:id>', method=['GET'])
def get_order_by_id(id):
    try:
        order = db.session.query(Order).filter(Order.id == id).first()
        return jsonify(order.get_order())
    except Exception as e:
        return f'{e}'


@app.route('/ooffers/', method=['GET'])
def get_all_offers():
    try:
        offers = db.session.query(Offer).all()
        return jsonify([offer.get_offer() for offer in offers])
    except Exception as e:
        return f'{e}'


@app.route('/ofers/<int:id>', method=['GET'])
def get_offer_by_id(id):
    try:
        offer = db.session.query(Offer).filter(Offer.id == id).first()
        return jsonify(offer.get_offer())
    except Exception as e:
        return f'{e}'

