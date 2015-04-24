from django.core.management.base import BaseCommand, CommandError
from mysite.models import Dutyreg, Extraworkreg, Holidutyreg, Variable
import datetime
class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        duty = Dutyreg()
        duty.save()
        extrawork = Extraworkreg()
        extrawork.save()
        holiduty = Holidutyreg()
        holiduty.save()
        self.stdout.write('OK!\n')
