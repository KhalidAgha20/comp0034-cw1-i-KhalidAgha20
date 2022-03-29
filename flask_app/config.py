class Config(object):
    SECRET_KEY = 'zrcpU_ln4RePGw0y6l0dOg'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ENV = 'production'


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    ENV = 'testing'
    DEBUG = True
    SQLALCHEMY_ECHO = True
