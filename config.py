import os
from dotenv import load_dotenv

load_dotenv()

class configuracao: 
    # Se existir DATABASE_URL, prioriza a conexão remota,
    # senão, usa a local (Docker) como fallback.
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or (
        f"postgresql://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@localhost:"
        f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
