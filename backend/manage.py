import os
from app import create_app
from app.database import db
from app.models import User


app = create_app(os.getenv('FLASK_BACKEND_CONFIG') or 'dev')


def make_shell_context():
    return dict(app=app, db=db, User=User)


if __name__ == '__main__':
    app.run()
