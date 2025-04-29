from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse('Hello World')
def api_view(request):
    return JsonResponse({'message':'Hello world'})
# Create your views here.
