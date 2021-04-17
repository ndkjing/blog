import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'metas.settings'   #项目settings配置
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
