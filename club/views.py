from django.shortcuts import render
from .models import Resource

# Create your views here.
def index(request):
    return render(request, 'club/index.html')
    
def resources(request):
    resource_list = Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list':resource_list})