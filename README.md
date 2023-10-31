# A basic Setup/Django Style to make django development faster and easier

## 1. First Create a django project
```console
django-admin startproject project_name
```

## 2. Now Modify your project_name/project_name/settings.py with settings.diff
```console
patch project_name/project_name/settings.py settings.diff
```
> Doing so will automatically update the `INSTALLED_APPS` and `MIDDLEWARE` list
    with custom apps and middleware
> NOTE:- App name and Middleware should follow this convestion
>> Appname:- nameApp/nameapp/name_app, should end with app/App/APP
>> Middleware:- namemiddleware/nameMiddleware/name_middleware, should end with M/middleware
>> also you can change then name convention latter after applying the patch,
    search for `# change me` lines
>> You can read `settings.py` for the actual result of how it should be and make small changes
    accordingly 

## 3. Now Modify your project_name/project_name/urls.py with main_urls.diff
```console
cp urls.py project_name/project_name/urls.py 
```
> Doing so will automatically include the urls from the all the apps, and no need to make changes 
     when creating new apps,
> It will also addes a wildcard url that will handels the 404 automatically you can change it's behaviour
    by modifing `fOf` function

## 4. Now adding a Urls.py file for apps,
```console
cp app/urls.py project_name/app_name/urls.py
```
> Doing so will create a urls.py file for app,which has following features:-
-   `SLUG` variable that holds the slug for the app,eg;-```SLUG='app_slug'```
    then `localhost:8000/app_slug/*` will be handled by app urls.py
-   `view_from_class()` function will create a appropirate sub_slug for each view_class in
    app/views.py, for view.py setup read step 5; such that `localhost:8000/app_slug/sub_slug`
    will be handled by view class in view.py direclty no need to modify urls.py again
    [If you are trying to use view_functions then it has no purpose you have to 
    update the urls.py yourself]

# 5. Guid on How to make a good looking readable app/views.py
```console
cp app/views.py project_name/app/views.py
```
> This view style will help you do easy modify and keep eveything under controll
```py
class Test(View):

    """
    This class handles the :-
        url/app_slug/test
    And it's template name is
        app_slug_test
    """
    __name__ = "test"
    __slug__ = "test"

    def get(self, request):
        return HttpResponse(b"I got a get requests")
```

### Now you have a proper setup of django and makes your django boring task automated