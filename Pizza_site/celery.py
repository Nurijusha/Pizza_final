
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pizza_site.settings')

app = Celery('Pizza_site')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'blog.tasks.send_view_count_report',
        'schedule': crontab(), # Выполнять еждневно в полночь.
    }
}
