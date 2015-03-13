from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.forms import ModelForm
from django.core.context_processors import csrf
from mysite.models import Registers,Extrawork
# Create your views here.
import time


def index(request):
    return HttpResponse('ok')


def admin(request):
    return HttpResponse('alright')
