import os


class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    DB_SERVER = '192.168.1.56'
    SECRET_KEY = 'marmota'

    @property
    def DATABASE_URI(self):  # Note: all caps
        return 'mysql://user@{}/foo'.format(self.DB_SERVER)


class ProductionConfig(Config):
    """Uses production database server."""
    DB_SERVER = '192.168.19.32'


class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    # DATABASE = os.path.join(INSTANCE_PATH, 'flaskr_dev.sqlite')


class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    # DATABASE_URI = 'sqlite:///:memory:'
    # DATABASE = os.path.join(self.instance_path, 'flaskr_testing.sqlite')


def get_config():
    config_type = os.environ.get('FLASK_ENV', 'development')
    if os.environ.get('FLASK_TESTING', False):
        return TestingConfig()

    if config_type == 'production':
        return ProductionConfig()

    return DevelopmentConfig()
