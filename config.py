class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3307/landingdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 300
    SECRET_KEY = "horrible_secret_key"