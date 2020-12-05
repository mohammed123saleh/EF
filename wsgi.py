"""
WSGI config for Travencia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
from django.core.management import call_command

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Travencia.settings')

application = get_wsgi_application()



'''

# add this block of code
try:
    import uwsgidecorators
    from django.core.management import call_command

    @uwsgidecorators.timer(10)
    def send_queued_mail(num):
        """Send queued mail every 10 seconds"""
        call_command('send_queued_mail', processes=1)

except ImportError:
    print("uwsgidecorators not found. Cron and timers are disabled")


   



def my_cron_job():
    call_command('send_queued_mail', processes=1)
print(my_cron_job())

''' 

from django.core.management import call_command

def my_cron_job():
    call_command('send_queued_mail', processes=1)

my_cron_job()
