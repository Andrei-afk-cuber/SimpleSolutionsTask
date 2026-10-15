from .celery_app import app


# get currency task
@app.task
def get_currency():
    pass