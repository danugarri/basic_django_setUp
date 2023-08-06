from django.http import HttpResponse

HTML_BODY = "<html><body></body></html>"
greeting = "<h1>Welcome to the Django Framework</h1>"


def set_basic_view(_):
    return HttpResponse(HTML_BODY + greeting)
