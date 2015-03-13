from django.db import models
import datetime
# Create your models here.


class Dutyreg(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today())
    amname = models.CharField(max_length=75)
    amamount = models.IntegerField(default=0)
    pmname = models.CharField(max_length=75)
    pmamount = models.IntegerField(default=0)
    evename = models.CharField(max_length=75)
    eveamount = models.IntegerField(default=0)
    remark = models.CharField(max_length=255)


class Extraworkreg(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today())
    amname = models.CharField(max_length=75)
    amtext = models.CharField(max_length=255)
    amamount = models.IntegerField(default=0)
    pmname = models.CharField(max_length=75)
    pmtext = models.CharField(max_length=255)
    pmamount = models.IntegerField(default=0)
    evename = models.CharField(max_length=75)
    evetext = models.CharField(max_length=255)
    eveamount = models.IntegerField(default=0)
    remark = models.CharField(max_length=255)
