import os

class BaseConfig(object):
    DEBUG = os.environ.get("DEBUG", False)

    DB_NAME = os.environ.get("POSTGRES_DB", "db")
    DB_USER = os.environ.get("POSTGRES_USER", "baonv")
    DB_PASS = os.environ.get("POSTGRES_PASSWORD", "baonv123")
    DB_PORT = os.environ.get("POSTGRES_PORT", 5432)

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@postgres:{DB_PORT}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


pass
