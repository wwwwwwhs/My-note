
"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``. 它将 ASGI 可调用程序公开为一个名为 ``application`` 的模块级变量。

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_asgi_application()
