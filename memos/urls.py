"""
URL configuration for memos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import sys

if 'makemigrations' not in sys.argv and 'migrate' not in sys.argv:
    from memos_backend.api import api
else:
    api = None  # apiをNoneに設定しておく

# 基本のURLパターン
urlpatterns = [
    path('admin/', admin.site.urls),
]

# apiが定義されているときだけ、APIのルートを追加
if api:
    urlpatterns += [path('api/', api.urls)]
