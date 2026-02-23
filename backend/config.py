
import os
from dotenv import load_dotenv
from util.singleton import singleton

load_dotenv()


@singleton
class Config:

    def __init__(self):
        env = os.environ.get('FLASK_ENV', 'development')

        cors_origins = os.environ.get('CORS_ORIGINS', '*')
        self.CORS_ORIGINS = cors_origins.split(',') if cors_origins != '*' else ['*']
        self.CORS_ALLOW_ALL = cors_origins == '*'

        self.FLASK_ENV = env
        self.DEBUG = env == 'development'
        self.TESTING = env == 'testing'
