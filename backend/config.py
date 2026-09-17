import os

class Settings:
    APP_NAME = "Akash AI"
    APP_VERSION = "1.0.0"

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    SEARCH_API_KEY = os.getenv("SEARCH_API_KEY", "")

settings = Settings()
