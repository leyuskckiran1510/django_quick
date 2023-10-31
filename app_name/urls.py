from django.urls import path
from . import views

SLUG = "org"


def _path(*args, name=None):
    return path(*args, name=f"{SLUG}_{name}")


def view_from_class():
    # Ignored for some issues 'options',
    methods = {"get", "post", "put", "patch", "delete", "head", "trace"}
    paths = []
    for cls in views.__dict__.values():
        if isinstance(cls, type):
            cls_keys = set(cls.__dict__.keys())
            if methods.intersection(cls_keys):
                paths.append(
                    _path(
                        cls.__dict__.get("__slug__"),
                        cls.as_view(),  # type:ignore
                        name=cls.__dict__.get("__name__"),
                    )
                )
    return paths


view_classes = view_from_class()
urlpatterns = [*view_classes]
