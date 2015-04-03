#-*- coding:utf-8 -*-
from django.db import models
import datetime
# Create your models here.


class Dutyreg(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today())
    amname = models.CharField(max_length=75,default=" ")
    amamount = models.IntegerField(default=100)
    pmname = models.CharField(max_length=75,default=" ")
    pmamount = models.IntegerField(default=100)
    evename = models.CharField(max_length=75,default=" ")
    eveamount = models.IntegerField(default=120)
    remark = models.CharField(max_length=255,default=" ")


class Extraworkreg(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today())
    amname = models.CharField(max_length=75,default=" ")
    amtext = models.CharField(max_length=255,default=" ")
    amamount = models.IntegerField(default=0)
    pmname = models.CharField(max_length=75,default=" ")
    pmtext = models.CharField(max_length=255,default=" ")
    pmamount = models.IntegerField(default=0)
    evename = models.CharField(max_length=75,default=" ")
    evetext = models.CharField(max_length=255,default=" ")
    eveamount = models.IntegerField(default=0)
    remark = models.CharField(max_length=255,default=" ")

class Holidutyreg(models.Model):
    id = models.AutoField(primary_key=True)
    date=models.DateField(default=datetime.date.today())
    emergencyteamname = models.CharField(max_length=75)
    emergencyteamamount = models.IntegerField(default=0)
    servicecentername = models.CharField(max_length=75)
    servicecenteramount = models.IntegerField(default=0)
    generaldutyname = models.CharField(max_length=75)
    generaldutyamount = models.IntegerField(default=0)
    amphonedutyname = models.CharField(max_length=75)
    amphonedutyamount = models.IntegerField(default=0)
    amengineername = models.CharField(max_length=75)
    amengineeramount = models.IntegerField(default=0)
    pmphonedutyname = models.CharField(max_length=75)
    pmphonedutyamount = models.IntegerField(default=0)
    pmengineername = models.CharField(max_length=75)
    pmengineeramount = models.IntegerField(default=0)
    evedutyname = models.CharField(max_length=75)
    evedutyamount = models.IntegerField(default=0)
    remark = models.CharField(max_length=255)

class  Variable(models.Model):
    varname = models.CharField(max_length=255) 
    varval = models.CharField(max_length=255)
