
from app.data import EventQueue, Postgres
from requests import Session
from redis import Redis

import logging
import config

database = Postgres(
    config.POSTGRES_USER,
    config.POSTGRES_PASSWORD,
    config.POSTGRES_HOST,
    config.POSTGRES_PORT
)

redis = Redis(
    config.REDIS_HOST,
    config.REDIS_PORT,
    config.REDIS_DB,
    config.REDIS_PASSWORD
)

events = EventQueue("spectator", redis)
logger = logging.getLogger("processor")
requests = Session()
