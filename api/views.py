from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def create_blocks(request):
    return HttpResponse("this is a block.")
