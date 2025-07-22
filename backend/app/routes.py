from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, JWTManager
from .database import db
from .models import User


jwt = JWTManager()

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/ping', methods=['GET'])
def pong():
    return jsonify({'pong': True})


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': "Пользователь с таким 'login' уже существует"}), 409

    pswd_hash = generate_password_hash(password)

    try:
        new_user = User(username=username, password_hash=pswd_hash)
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 409

    return jsonify({'message': "Пользователь {} зарегистрирован".format(new_user.username)}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'message': "Ошибка при аутентификации"}), 401

    access_token = create_access_token(identity=user.id)
    res = {
        'message': "Вы авторизовались как {}".format(user.username),
        'access_token': access_token,
    }
    return jsonify(res), 200
