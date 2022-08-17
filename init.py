import os
from pathlib import Path
from dotenv import load_dotenv
from app.db import log
from sqlalchemy import create_engine, MetaData

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / '.env')

DEBUG = int(os.getenv('DEBUG'))

DATABASE_URI = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

meta = MetaData()

engine = create_engine(DATABASE_URI, echo=True)
meta.create_all(engine, tables=[log])
