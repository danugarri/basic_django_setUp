from django.http import HttpResponse
from django.urls import reverse

HTML_BODY = "<html><body></body></html>"
GREETING = "<h1>Welcome to the Django Framework</h1>"

DJANGO_REDIRECTION = '<a href="https://www.djangoproject.com/">Django</a>'
LOGIN = '<a href="/admin/">Login</a>'


def root(_):
    REDIRECT_TO_GREETING = f'<a href="{reverse("greeting")}">greeting</a>'
    return HttpResponse(
        HTML_BODY
        + "<ul>"
        + "<li>"
        + DJANGO_REDIRECTION
        + "</li>"
        + "<li>"
        + REDIRECT_TO_GREETING
        + "</li>"
        + "<li>"
        + LOGIN
        + "</li>"
    )


def set_basic_view(_):
    BACK = f'<a href="{reverse("root")}">Go Back</a>'
    return HttpResponse(HTML_BODY + GREETING + "</br>" + BACK)
