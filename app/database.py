import os
from dotenv import load_dotenv
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

TORTOISE_ORM = {
    "connections": {
        "default": DATABASE_URL,
    },
    "apps": {
        "models": {
            "models": ["app.models.user", "aerich.models"],  # aerich.models 꼭 포함
            "default_connection": "default",
        }
    },
}

def init_db(app: FastAPI):
    register_tortoise(
        app,
        db_url=DATABASE_URL,
        modules={"models": ["app.models.user"]},
        generate_schemas=False,  # aerich를 사용하니까 False로
        add_exception_handlers=True,
    )