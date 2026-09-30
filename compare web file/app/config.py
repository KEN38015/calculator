import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    app_name: str = "HTMX + FastAPI Starter"
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    api_key_prefix: str = os.getenv("API_KEY_PREFIX", "sk_live_")


settings = Settings()
