from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world, this is like home page or smth uk")
