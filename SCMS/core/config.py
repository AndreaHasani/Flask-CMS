import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:toor@localhost/testing'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(24)
    WTF_CSRF_SECRET_KEY = os.urandom(24)

    # Debug
    DEBUG = True
    WTF_CSRF_ENABLED = False

    #Static Files
    ADMIN_STATIC = "./static/"
