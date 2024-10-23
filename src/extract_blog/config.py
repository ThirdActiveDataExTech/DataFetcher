import os
from dotenv import load_dotenv


load_dotenv()

APP_HOME = os.getenv('APP_HOME', '/')
APP_NAME = os.getenv('APP_NAME')
LOG_DIR = os.getenv('APP_LOG_DIR', os.path.join(APP_HOME, 'logs'))

BASE_PATH = os.getenv('BASE_PATH')

META_DB_PATH = os.getenv('META_DB_PATH')
URL_DB_PATH = os.getenv('URL_DB_PATH')