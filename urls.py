from django.contrib import admin
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import include, path, re_path

from .settings import CUSTOM_APPS, FILE404HTML


def apps_urls():
    _urls = []
    for i in CUSTOM_APPS:
        try:
            _app = __import__(f"{i}.urls")
            _urls.append(path(f"{_app.urls.SLUG}", include(f"{i}.urls")))
            _urls.append(path(f"{_app.urls.SLUG}/", include(f"{i}.urls")))
        except ImportError as error:
            print(
                "Please Create A GLOBAL `SLUG` variable with it's url"
                "value in app_name/urls.py to include the path of the app in global urls"
                f"\n[ERROR]:{error}"
            )
    return _urls


def fOf(request):
    if FILE404HTML:
        return render(request, FILE404HTML)
    return HttpResponseNotFound(b"404: Page Not Found")


FEATURE_URLS = []
STATIC_URLS = []
CUSTOM_APPS_URLS = apps_urls()
DJANGOS_URLS = [path("admin/", admin.site.urls)]
FOUR_O_FOUR = [re_path("[^/]*", fOf)]

urlpatterns = DJANGOS_URLS + FEATURE_URLS + CUSTOM_APPS_URLS + STATIC_URLS + FOUR_O_FOUR
