from os import environ, path


__all__ = ["settings"]


class Settings:
    """
    Settings class
    """
    BASE_DIR: str = path.abspath(path.join(path.dirname(__file__), '..'))

    POSTGRES_DB: str = environ.get("POSTGRES_DB")
    POSTGRES_USER: str = environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST")
    POSTGRES_PORT: int = environ.get("POSTGRES_PORT")
    
    DEBUG: bool = environ.get("DEBUG") == "1"
     

settings = Settings()
