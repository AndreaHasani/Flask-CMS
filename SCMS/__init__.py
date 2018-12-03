from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from SCMS.core.config import Config
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(Config)
    login_manager.init_app(application)
    csrf.init_app(application)
    db.init_app(application)

    # from SCMS.core.posts import posts
    with application.app_context():
        from SCMS.core.users.view import users
        from SCMS.views import main

        from SCMS.core.models import Users, Role

        db.drop_all()
        hashPassword = generate_password_hash(
            'admin12345', method='sha256')
        db.create_all()
        admin = Users('admin', 'admin@example.com', hashPassword)
        admin_role = Role(name='admin')
        reader_role = Role(name='reader')
        author_role = Role(name='author')
        db.session.commit()
        admin.roles = [admin_role, author_role, reader_role]

        db.session.add(admin)
        db.session.commit()

    application.register_blueprint(users, url_prefix='/admin')
    application.register_blueprint(main)
    # application.register_blueprint(posts)

    return application
