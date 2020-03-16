from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    myDict = {'insert_me':"wow dit is exact hetzelfde als met php yaml files"}
    return render(request, 'noviwebshopapp/index.html', context=myDict)
