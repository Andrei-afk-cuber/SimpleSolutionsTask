import os
from dataclasses import dataclass

import dotenv

dotenv.load_dotenv()


@dataclass
class DBConfig:
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")


@dataclass
class RedisConfig:
    host = os.getenv("REDIS_HOST")
    port = os.getenv("REDIS_PORT")
    user = os.getenv("REDIS_USER")
    password = os.getenv("REDIS_PASSWORD")