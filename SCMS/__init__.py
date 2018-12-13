from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from SCMS.core.dynaconf import configure_dynaconf
from werkzeug.security import generate_password_hash, check_password_hash
from SCMS.tests.simulate import fakePosts
from SCMS.core import configure_extensions, configure_extension
from os import urandom

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager = LoginManager()
api = Api(prefix='/api/v1')


def create_app():
    application = Flask(__name__)
    application.config["SECRET_KEY"] = urandom(24)
    configure_dynaconf(application)
    login_manager.init_app(application)
    csrf.init_app(application)
    db.init_app(application)

    # from SCMS.core.posts import posts
    with application.app_context():
        # Import blueprint
        from SCMS.core.users.view import users
        from SCMS.views import main

        # Import Models
        from SCMS.core.models import Users, Role, Posts

        # Import Restful Api
        from SCMS.core.api.posts import edit as post_edit_api

        # Create Test login
        db.drop_all()
        hashPassword = generate_password_hash(
            'admin12345', method='sha256')
        db.create_all()
        admin = Users(username='admin', email='admin@example.com',
                      password=hashPassword)
        admin_role = Role(name='admin')
        reader_role = Role(name='reader')
        author_role = Role(name='author')
        db.session.commit()
        admin.roles = [admin_role, author_role, reader_role]

        db.session.add(admin)
        db.session.commit()

        # Fake posts
        fakePosts(db, Posts)
        configure_extensions(application)

    application.register_blueprint(users, url_prefix='/admin')
    application.register_blueprint(main)
    # application.register_blueprint(posts)

    # Register Api
    api.add_resource(post_edit_api, "/posts/edit")

    # Some library like to get init after
    api.init_app(application)

    return application
