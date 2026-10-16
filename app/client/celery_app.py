from celery import Celery
from celery.schedules import crontab

from ..config import RedisConfig

# Celery app
app = Celery(
    'app',
    broker=f'redis://{RedisConfig.host}:{RedisConfig.port}/0',
    include=['app.client.tasks']
)


# update celery config
app.conf.update(
    timezone='UTC',
    enable_utc=True,
)


# update scheduler config
app.conf.beat_schedule = {
    "currency-price-per-minute": {
        "task": "app.client.tasks.get_currency_task",
        "schedule": crontab(),
    },
}