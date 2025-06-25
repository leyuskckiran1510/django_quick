# Better way to program in django
If you are tyring to build api based django project then don't even look at this, [django-ninja](https://django-ninja.dev/) is best of best.
1. ## First Create a django project
```bash
django-admin startproject project_name
```
------

2. ## Now Modify your `project_name/project_name/settings.py` as
- automatically tries to render the file provided here; incase of filenotfound
```py
FILE404HTML=""
#FILE404HTML = "404.html"
```
- dynamically add app to your installed app list, if the app names ends with `_app`
    - if you like to modify that, change the `auto_install_app(your_suffix)`
```diff
-    INSTALLED_APPS  = [
-       "django.contrib.admin",
-       "django.contrib.auth",
-       "django.contrib.contenttypes",
-       "django.contrib.sessions",
-       "django.contrib.messages",
-       "django.contrib.staticfiles",
-   ]
```
```py
def auto_install_app(app_suffix: str = "_app"):
    __xs = []
    for i in os.listdir(BASE_DIR):
        app_path = os.path.join(BASE_DIR, i)
        if os.path.isdir(app_path) and i.lower().endswith(app_suffix):
            __xs.append(i)
    return __xs


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
CUSTOM_APPS = auto_install_app("_app")
INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS
```
- dynamically add middleware apps to your installed middlewares list 
```diff
-DJANGO_MIDDLEWARE = [
-    "django.middleware.security.SecurityMiddleware",
-    "django.contrib.sessions.middleware.SessionMiddleware",
-    "django.middleware.common.CommonMiddleware",
-    "django.middleware.csrf.CsrfViewMiddleware",
-    "django.contrib.auth.middleware.AuthenticationMiddleware",
-    "django.contrib.messages.middleware.MessageMiddleware",
-    "django.middleware.clickjacking.XFrameOptionsMiddleware",
-]
```
```py
DJANGO_MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CUSTOM_MIDDLEWARE = auto_install_app("middleware")
MIDDLEWARE = DJANGO_MIDDLEWARE + CUSTOM_MIDDLEWARE
```
------

3. ## Now copy the content of [urls.py](./urls.py) to `project_name/project_name/urls.py`
- automatically loads the `urls.py` of all installed apps
```bash
cp app/urls.py project_name/app_name/urls.py
```

------
4. ## Now create your app with 
- creates a django-app with costume template, that is compitable with above changes
```bash
python manage.py startapp --template=https://github.com/leyuskckiran1510/django-app-stater/archive/master.zip login_app
```
- now it will populate `login_app`'s `urls.py` with code that automaticall, generates url for app and it's view
    - Doing so will create a urls.py file for app,which has following features:-
    -   `SLUG` variable that holds the slug for the app,eg;-```SLUG='app_slug'``` then `localhost:8000/app_slug/*` will be handled by app urls.py
    -   `view_from_class()` function will create a appropirate sub_slug for each view_class in
    `app/views.py`, such that `localhost:8000/app_slug/sub_slug`
    will be handled by view class in `view.py` direclty no need to modify `urls.py` again
    [If you are trying to use view_functions then it has no purpose you have to 
    update the urls.py yourself]
    - `views.py` has a simple demo view class showing the usecase, demo at #6

5. ## creating new app after the template is used
- once you have created app with template you can just do following
```bash
python manage.py startapp2 home_app
```
- now this time new command is added to `manage.py` as `startapp2` which handels the templating part itself

------

6. ## Inside of app/views.py
```py
from django.http import HttpResponse
from django.views import View


class LoginAppView(View):

    """
    This class handles the :-
        url/login_app/{__slug__}
    and the url name for template is such
        login_app_{__url_name__}
    """

    __url_name__ = "login_app"
    __slug__ = "login_app_slug"

    def get(self, request):
        return HttpResponse(b"I got a get requests")
```
- this class is excatly same django-view class, only the two, class-level attibute is added
    - which does following
        - `__url_name__`:- it denotes the url name, for refrenceing on templates and other places
        - `__slug__`:- it denotes the url for the view, following the app name

> Now you have a proper setup of django and makes your django boring task automated