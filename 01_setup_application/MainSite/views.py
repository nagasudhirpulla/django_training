from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context={"name":"John"}
    return render(request, 'index.html.j2', context)
    # return render(request, 'App2/index.html.j2', context)
    # return HttpResponse("hello World")