#-*- coding:utf-8 -*-
from django.db import models
import datetime
# Create your models here.


class Dutyreg(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today())
    amname = models.CharField(max_length=75,default=" ")
    amamount = models.IntegerField(default=0)
    pmname = models.CharField(max_length=75,default=" ")
    pmamount = models.IntegerField(default=0)
    evename = models.CharField(max_length=75,default=" ")
    eveamount = models.IntegerField(default=0)
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
