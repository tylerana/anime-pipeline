import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_db_connection():
   user = os.getenv("DB_USER", "user")
   password = os.getenv("DB_PASS", "pass")
   host = os.getenv("DB_host", "db")
   db_name = os.getenv("DB_NAME", "name")
   port = os.getenv("DB_PORT", "5432")
   
   # postgresql://user:password@host:port/database
   url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
    
    #engine creation
   engine = create_engine(url)
   return engine