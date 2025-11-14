from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.
def members(request):
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())    
    mymembers = Member.objects.all().values()
    context = {
        'mymembers' : mymembers,    
    }
    return render(request, 'all_members.html', context)

def details(request, id):
    mymember = Member.objects.get(id=id)
    context = {
        'mymember' : mymember
    }
    return render(request, 'details.html', context)
    
def main(request):
    return render(request, 'main.html')

def testing(request):
    context = {
        'fruits' : ['Apple', 'Banana', 'Orange'],
    }

    return render(request, 'template.html', context)