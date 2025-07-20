# классы моделей, отражающие структуру таблиц БД

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)  # уникальный ключ
    created_at = db.Column(db.DateTime, default=datetime.now)  # момент регистрации
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # указание на внешний ключ в таблице role (колонка - id)
    login = db.Column(db.String(80), unique=True, nullable=False)  # логин пользователя
    password_hash = db.Column(db.String(128), nullable=False)  # пароль (hash)
    approved = db.Column(db.Boolean, default=False)  # разрешение доступа к данным со стороны администратора

    role = db.relationship('Role', backref='users')

    def __repr__(self):
        return f"<User: id={self.id}, login={self.login}, role_id={self.role_id}>"


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)  # уникальный ключ
    role = db.Column(db.String(80), unique=True, nullable=False)  # роль

    def __repr__(self):
        return f"<Role: id={self.id}, role={self.role}>"