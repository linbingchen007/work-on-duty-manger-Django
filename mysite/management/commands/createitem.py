from django.core.management.base import BaseCommand, CommandError
from mysite.models import Dutyreg, Extraworkreg, Holidutyreg, Variable
import datetime
class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        curdate = datetime.date(2015, 5, 1)
        delta = datetime.timedelta(days=1)
        while curdate <= datetime.date(2035, 5, 1):
            queryresults = Dutyreg.objects.all().filter(date=curdate)
            if len(queryresults)==0:
                duty = Dutyreg(date=curdate)
                duty.save()
            queryresults = Extraworkreg.objects.all().filter(date=curdate)
            if len(queryresults)==0:
                extrawork = Extraworkreg(date=curdate)
                extrawork.save()
            queryresults = Holidutyreg.objects.all().filter(date=curdate)
            if len(queryresults)==0:
                holiduty = Holidutyreg(date=curdate)
                holiduty.save()
            curdate += delta
        self.stdout.write('OK!\n')
