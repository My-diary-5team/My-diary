import os
from dotenv import load_dotenv

# 개발환경이면 .env, 배포환경이면 .env.prod
env = os.getenv("ENVIRONMENT", "dev")

if env == "prod":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env")

DATABASE_URL = os.getenv("DATABASE_URL")
DEBUG = os.getenv("DEBUG") == "True"
SECRET_KEY = os.getenv("SECRET_KEY")
