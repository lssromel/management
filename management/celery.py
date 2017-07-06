from __future__ import absolute_import
 
import os
 
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'management.settings') #Nota 1
 
from django.conf import settings  # Nota 2
 
app = Celery('CeleryApp') #Nota 3
 
app.config_from_object('django.conf:settings') #Nota 4
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) #Nota 5
 
app.conf.update(
    BROKER_URL = 'django://',CELERY_RESULT_BACKEND='amqp', #Nota 6
)
