
from app.data import EventQueue
from redis import Redis

import config

redis = Redis(
    config.REDIS_HOST,
    config.REDIS_PORT,
    config.REDIS_DB,
    config.REDIS_PASSWORD
)

events = EventQueue("spectator", redis)
