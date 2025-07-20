# конфигурационный файл серверной части

import os

basedir = os.path.abspath(os.path.dirname(__file__))  # определяем базовую директорию для серверной части

class Config:
    """
    Конфигурация для серверной части
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-default-secret-key'  # секретный ключ через окружение (или в случае отсутствия формируем default value)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or ('sqlite:///' + os.path.join(basedir, 'UAV_data.sqlite'))  # указатель на рабочую БД (или в случае ее отсутствия default value)
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # отключает слежение SQLAlchemy за объектами, снижает память и предупреждение
