import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'default-secret-key'
    JWT_SECRET_KEY = 'jwt-default-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(Config.BASE_DIR, 'uav_knowledge.db'))


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
}
