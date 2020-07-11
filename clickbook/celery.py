import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clickbook.settings')

app = Celery('clickbook')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    result_expires=timedelta(seconds=15),
    result_persistent=True,
)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
