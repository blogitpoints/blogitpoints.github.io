from flaskblog import localsettings

class Config:
    SECRET_KEY = localsettings.SECRET_KEY
    SQLALCHEMY_DATABASE_URI = localsettings.SQLALCHEMY_DATABASE_URI
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = localsettings.MAIL_USERNAME
    MAIL_PASSWORD = localsettings.MAIL_PASSWORD
    