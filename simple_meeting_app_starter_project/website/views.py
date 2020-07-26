# from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to Homee  Page")


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("About Page")


# Create your views here.
