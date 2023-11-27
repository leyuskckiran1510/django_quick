from django.urls import path
from . import views
from django.views import View

SLUG = "test"  # app_slug_name


def _path(*args, name=None):
    return path(*args, name=f"{SLUG}_{name}")


def check_slug(cls, key) -> str:
    res = cls.__dict__.get(key)
    if res:
        return res
    else:
        raise ValueError(f"__slug__ is not provided for the view class [{cls}]\n")


def view_from_class():
    paths = []
    for cls in views.__dict__.values():
        if isinstance(cls, type) and issubclass(cls, View) and View != cls:
            if issubclass(cls, View):
                paths.append(
                    _path(
                        check_slug(cls, "__slug__"),
                        cls.as_view(),
                        name=cls.__dict__.get("__name__", cls.__dict__.get("__slug__")),
                    )
                )
    return paths


view_classes = view_from_class()
urlpatterns = [*view_classes]
