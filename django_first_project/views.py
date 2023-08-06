from django.http import HttpResponse

HTML_BODY = "<html><body></body></html>"
GREETING = "<h1>Welcome to the Django Framework</h1>"
BASIC_REDIRECTION = '<a href="https://www.google.com">Link</a> '


def root(_):
    return HttpResponse(HTML_BODY + BASIC_REDIRECTION)


def set_basic_view(_):
    return HttpResponse(HTML_BODY + GREETING)
