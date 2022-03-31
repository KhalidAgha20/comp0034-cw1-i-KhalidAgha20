import pathlib


class Config(object):
    SECRET_KEY = 'zrcpU_ln4RePGw0y6l0dOg'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class ProductionConfig(Config):
    ENV = 'production'


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True

    DATA_PATH = pathlib.Path(__file__).parent.parent
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(DATA_PATH.joinpath('myflask.sqlite'))


class TestingConfig(Config):
    ENV = 'testing'
    DEBUG = True
    SQLALCHEMY_ECHO = True


x = pathlib.Path(__file__).parent.parent.joinpath("data")
print(x)
print('sqlite:///' + str(x.joinpath('myflask.sqlite')))
