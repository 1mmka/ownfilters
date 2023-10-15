from django.shortcuts import render
from mainapp.models import Human

# Create your views here.
def index(request):
    return render(request,'home.html',{'dct':Human.objects.all()})