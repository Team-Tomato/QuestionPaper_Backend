import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

def get_env_variable(name):
  try:
    return os.getenv(name)
  except KeyError:
    message = "Expected environment variable '{}' not set.".format(name)
    raise Exception(message)

# the values of those depend on your setup
POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
  DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
  SQLALCHEMY_DATABASE_URI = DB_URL
  DEBUG = False


class StagingConfig(Config):
  DEVELOPMENT = True
  DEBUG = True


class DevelopmentConfig(Config):
  DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
  SQLALCHEMY_DATABASE_URI = DB_URL
  DEVELOPMENT = True
  DEBUG = True


class TestingConfig(Config):
  TESTING = True