from flask import Flask, jsonify, request, abort
from config import Config
from models import User, Offer, Order
from insert import data_db
from init_db import db


app = Flask(__name__)


@app.route('/users/', methods=['GET', 'POST'])
def get_all_users():
    if request.method == 'GET':
        try:
            users = db.session.query(User).all()
            return jsonify([user.to_dict() for user in users])
        except Exception as e:
            return f'{e}'
    elif request.method == "POST":
        data = request.json
        db.session.add(User(**data))
        db.session.commit()

        return jsonify(code=200)


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(user_id):
    if request.method == 'GET':
        try:
            user = db.session.query(User).filter(User.id == user_id).first()
            return jsonify(user.to_dict())
        except Exception as e:
            return f'{e}'

    elif request.method == 'PUT':
        user = db.session.query(User).filter(User.id == user_id).first()

        if user is None:
            abort(404)

        db.session.query(User).filter(User.id == user_id).update(request.json)
        db.session.commit()

        return jsonify(code=200)

    elif request.method == 'DELETE':
        count = db.session.query(User).filter(User.id == id).delete()
        db.session.commit()
        if not count:
            abort(404)
        return jsonify(code=200)


@app.route('/orders/', methods=['GET', 'POST'])
def get_all_orders():
    if request.method == 'GET':
        try:
            orders = db.session.query(Order).all()
            return jsonify([order.get_order() for order in orders])
        except Exception as e:
            return f'{e}'
    elif request.method == "POST":
        data = request.json
        db.session.add(Order(**data))
        db.session.commit()

        return jsonify(code=200)


@app.route('/orders/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_order_by_id(id):
    if request.method == 'GET':
        try:
            order = db.session.query(Order).filter(Order.id == id).first()
            return jsonify(order.get_order())
        except Exception as e:
            return f'{e}'

    elif request.method == 'PUT':
        order = db.session.query(Order).filter(Order.id == id).first()

        if order is None:
            abort(404)

        db.session.query(Order).filter(Order.id == id).update(request.json)
        db.session.commit()

        return jsonify(code=200)

    elif request.method == 'DELETE':
        count = db.session.query(Order).filter(Order.id == id).delete()
        db.session.commit()
        if not count:
            abort(404)
        return jsonify(code=200)


@app.route('/ooffers/', methods=['GET', 'POST'])
def get_all_offers():
    if request.method == 'GET':
        try:
            offers = db.session.query(Offer).all()
            return jsonify([offer.get_offer() for offer in offers])
        except Exception as e:
            return f'{e}'
    elif request.method == "POST":
        data = request.json
        db.session.add(Offer(**data))
        db.session.commit()

        return jsonify(code=200)


@app.route('/ofers/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(id):
    if request.method == 'GET':
        try:
            offer = db.session.query(Offer).filter(Offer.id == id).first()
            return jsonify(offer.get_offer())
        except Exception as e:
            return f'{e}'

    elif request.method == 'PUT':
        offer = db.session.query(Offer).filter(Offer.id == id).first()

        if offer is None:
            abort(404)

        db.session.query(Offer).filter(Offer.id == id).update(request.json)
        db.session.commit()

        return jsonify(code=200)

    elif request.method == 'DELETE':
        count = db.session.query(Offer).filter(Offer.id == id).delete()
        db.session.commit()
        if not count:
            abort(404)
        return jsonify(code=200)


if __name__ == '__main__':
    app.config.from_object(Config())

    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()
        data_db()

    app.run()
