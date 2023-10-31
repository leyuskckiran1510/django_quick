"""
URL configuration for te project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from core.settings import CUSTOM_APPS
from django.http import HttpResponseForbidden


def apps_urls():
    _urls = []
    for i in CUSTOM_APPS:
        try:
            _app = __import__(f"{i}.urls")
            print(_app.urls.SLUG)
            _urls.append(path(f"{_app.urls.SLUG}/", include(f"{i}.urls")))
        except ImportError as error:
            print(
                "Please Create A GLOBAL `SLUG` variable with it's url"
                "value in app_name/urls.py to include the path of the app in global urls"
                f"\n[ERROR]:{error}"
            )
    return _urls


def fOf(*_):
    return HttpResponseForbidden(b"The Url Is not Valid")


DJANGOS_URLS = [path("admin/", admin.site.urls)]
FEATURE_URLS = []
CUSTOM_APPS_URLS = apps_urls()
STATIC_URLS = []
FOUR_O_FOUR = [re_path("[^/]*", fOf)]

urlpatterns = DJANGOS_URLS + FEATURE_URLS + CUSTOM_APPS_URLS + STATIC_URLS + FOUR_O_FOUR
