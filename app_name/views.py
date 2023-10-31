from django.http import HttpResponse
from django.views import View


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


class Home(View):

    """
    This class handles the :-
        url/app_slug
    And it's template name is
        app_slug_index
    """

    __name__ = "index"
    __slug__ = ""

    def get(self, request):
        return HttpResponse(b"This is home page")


class Login(View):
    """
    This class handles the :-
        url/app_slug/login
    And it's template name is
        app_slug_login
    """

    __name__ = "login"
    __slug__ = __name__

    def get(self, request):
        return HttpResponse(b"Please Put your auth values")

    def post(self, request):
        return HttpResponse(b"This is Post Response")
