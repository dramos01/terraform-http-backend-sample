class Config(object):
    DB_FILE = 'terraform.db'

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass