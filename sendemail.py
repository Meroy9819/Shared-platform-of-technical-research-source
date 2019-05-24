import os
from django.core.mail import send_mail
import os
assert 'SYSTEMROOT' in os.environ
os.environ['DJANGO_SETTINGS_MODULE'] = 'codePlat.settings'

if __name__ == '__main__':
    send_mail('Subject here', 'Here is the message.', 'miaoran9819@163.com',
              ['miaoran9819@163.com'], fail_silently=False)