import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

DEBUG = int(os.getenv('DEBUG'))

DSN = "postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

DATABASE_URI = DSN.format(
    DB_USERNAME=os.getenv('DB_USERNAME'),
    DB_PASSWORD=os.getenv('DB_PASSWORD'),
    DB_HOST=os.getenv('DB_HOST'),
    DB_PORT=os.getenv('DB_PORT'),
    DB_NAME=os.getenv('DB_NAME')
)


def config():
    return {
        'DATABASE_URL': DATABASE_URI,
        'DEBUG': DEBUG,
        'APP_HOST': os.getenv('APP_HOST'),
        'APP_PORT': os.getenv('APP_PORT')
    }
