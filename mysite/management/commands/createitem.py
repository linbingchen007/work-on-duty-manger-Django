from django.core.management.base import BaseCommand, CommandError
from mysite.models import Dutyreg, Extraworkreg, Holidutyreg, Variable
import datetime
class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        queryresults = Dutyreg.objects.all().filter(date=datetime.date.today())
        if len(queryresults)==0:
            duty = Dutyreg()
            duty.save()
        queryresults = Extraworkreg.objects.all().filter(date=datetime.date.today())
        if len(queryresults)==0:
            extrawork = Extraworkreg()
            extrawork.save()
        queryresults = Holidutyreg.objects.all().filter(date=datetime.date.today())
        if len(queryresults)==0:
            holiduty = Holidutyreg()
            holiduty.save()
        self.stdout.write('OK!\n')
