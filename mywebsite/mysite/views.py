from django.http import HttpResponse

def hellp(request):
    return HttpResponse("Hello world")
