from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<p>blog home<p>')


def about(request):
    return HttpResponse('<p>blog about<p>')
