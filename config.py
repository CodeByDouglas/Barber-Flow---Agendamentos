import os
from dotenv import load_dotenv

load_dotenv()

class configuracao: 
    SQLALCHEMY_DATABASE_URI =  f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
