import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True
    CACHE_TYPE = os.environ.get('CACHE_TYPE')
    CACHE_REDIS_HOST = os.environ.get('CACHE_REDIS_HOST')
    CACHE_REDIS_PORT= os.environ.get('CACHE_REDIS_PORT')
    CACHE_REDIS_DB = os.environ.get('CACHE_REDIS_DB')
    CACHE_REDIS_URL= os.environ.get('CACHE_REDIS_URL')
