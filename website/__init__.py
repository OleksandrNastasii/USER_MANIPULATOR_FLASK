from flask import Flask, request, jsonify
from .models import UserModel
from .database import db_session, init_db

def create_app():
    app = Flask(__name__)
    init_db()

    @app.route('/users', methods=['POST'])
    def create_user():
        user_data = request.get_json()
        new_user = UserModel(**user_data)
        db_session.add(new_user)
        db_session.commit()
        return jsonify(user_data), 201

    @app.route('/users', methods=['GET'])
    def get_users():
        users = UserModel.query.all()
        return jsonify([user.show_user() for user in users]), 200

    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = UserModel.query.get(user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        return jsonify(user.show_user()), 200

    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user = UserModel.query.get(user_id)
        user_data = request.get_json()
        for key, value in user_data.items():
            setattr(user, key, value)
        db_session.commit()
        return jsonify(user.show_user()), 200

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = UserModel.query.get(user_id)
        db_session.delete(user)
        db_session.commit()
        return jsonify({"message": "User deleted"}), 200
    
    return app