from app import create_app
import os

# Configuration Options
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ooooooh secret'
    
    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

configs = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProductionConfig
}

# Flask App Setup
if os.getenv('FLASK_CONFIG') is not None:
    app = create_app(configs[os.getenv('FLASK_CONFIG')])
else:
    app = create_app(DevConfig)
