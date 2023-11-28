from django.http import HttpResponse
from django.core.serializers import serialize

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")