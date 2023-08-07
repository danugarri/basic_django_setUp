from django.shortcuts import render


def root(request):
    return render(request, "root_template.html")


def set_basic_view(request):
    return render(request, "greeting_template.html")
