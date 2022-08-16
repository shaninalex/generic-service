import os
from pathlib import Path

from app.db import create_tables
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / '.env')

DEBUG = int(os.getenv('DEBUG'))

DATABASE_URI = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

create_tables(database_uri=DATABASE_URI, echo=DEBUG)
