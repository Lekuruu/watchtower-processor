
from app.data import EventQueue, Postgres
from redis import Redis

import config

postgres = Postgres(
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
