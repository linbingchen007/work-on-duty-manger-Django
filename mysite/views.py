# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.forms import ModelForm
from django.core.context_processors import csrf
from mysite.models import Dutyreg, Extraworkreg
# Create your views here.
import time
import datetime


def makedutyreg(request):
    queryresults = Dutyreg.objects.all().filter(date=datetime.date.today())
    if len(queryresults) > 0:
        duty = queryresults[0]
    else:
        duty = Dutyreg()
        duty.save()
    c = {'duty': duty,
         }
    return render_to_response(
        'mysite/duty.html', c, context_instance=RequestContext(request))


def makeextraworkreg(request):
    queryresults = Extraworkreg.objects.all().filter(date=datetime.date.today())
    if len(queryresults) > 0:
        extrawork = queryresults[0]
    else:
        extrawork = Extraworkreg()
        extrawork.save()
    c = {'extrawork': extrawork,
         }
    return render_to_response(
        'mysite/extrawork.html', c, context_instance=RequestContext(request))


def response_success(request,retlink):
    msgtext = "提交成功!"
    c = {"msgtext": msgtext,
         "retlink": retlink,
         }
    return render_to_response('mysite/msgbox.html', c, context_instance=RequestContext(request))


def response_wrong(request,retlink):
    msgtext = "未知错误，请按格式填写。"
    c = {"msgtext": msgtext,
         "retlink": retlink,
         }
    return render_to_response('mysite/msgbox.html', c, context_instance=RequestContext(request))


def handleduty(request):
    queryresults = Dutyreg.objects.all().filter(date=datetime.date.today())
    msgtext = ""
    if len(queryresults) > 0:
        try:
            cur_duty = queryresults[0]
            cur_duty.amname = request.POST['amname']
            cur_duty.amamount = int(request.POST['amamount'])
            cur_duty.pmname = request.POST['pmname']
            cur_duty.pmamount = int(request.POST['pmamount'])
            cur_duty.evename = request.POST['evename']
            cur_duty.eveamount = int(request.POST['eveamount'])
            if request.POST['remark'].strip() != "":
                if cur_duty.remark == ' ':
                    cur_duty.remark +=  (request.POST['remark'])
                else:
                    cur_duty.remark += ' | ' + (request.POST['remark'])
            cur_duty.save()
        except:
            return response_wrong(request,'dj:duty')
    else:
        return response_wrong(request,'dj:duty')
    return response_success(request,'dj:duty')


def handleextrawork(request):
    queryresults = Extraworkreg.objects.all().filter(
        date=datetime.date.today())
    msgtext = ""
    if len(queryresults) > 0:
        try:
            cur_extrawork = queryresults[0]
            cur_extrawork.amname = request.POST['amname']
            cur_extrawork.amtext = request.POST['amtext']
            cur_extrawork.amamount = int(request.POST['amamount'])
            cur_extrawork.pmname = request.POST['pmname']
            cur_extrawork.pmtext = request.POST['pmtext']
            cur_extrawork.pmamount = int(request.POST['pmamount'])
            cur_extrawork.evename = request.POST['evename']
            cur_extrawork.evetext = request.POST['evetext']
            cur_extrawork.eveamount = int(request.POST['eveamount'])
            if request.POST['remark'].strip() != "":
                if cur_extrawork.remark==' ':
                    cur_extrawork.remark += (request.POST['remark'])
                else:
                    cur_extrawork.remark += ' | ' + (request.POST['remark'])
            cur_extrawork.save()
        except:
            return response_wrong(request,'dj:extrawork')
    else:
        return response_wrong(request,'dj:extrawork')
    return response_success(request,'dj:extrawork')


def index(request):
    return render_to_response('mysite/index.html',context_instance=RequestContext(request))
    # return render_to_response('mysite/duty.html',
    # context_instance=RequestContext(request))


def duty(request):
    return makedutyreg(request)
def extrawork(request):
    return makeextraworkreg(request)

def admin(request):
    return HttpResponse('alr')
