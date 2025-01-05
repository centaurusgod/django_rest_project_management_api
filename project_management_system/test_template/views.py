from django.http import HttpResponse, request

def index(request):
    return HttpResponse('<h1>Hello World Tilak and ozone</h1>')