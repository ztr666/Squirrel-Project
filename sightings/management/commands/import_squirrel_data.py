import csv
import datetime
from django.core.management.base import BaseCommand
from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Import squirrel data'
    def add_arguments(self, parser):
        parser.add_argument('path', help='rows.csv')
    def handle(self, *args, **options):
        file_ = options['path']
        with open(file_) as fp:
            reader = csv.DictReader(fp)
            data=list(reader)
            for item in data:
                obj = Squirrel()
                obj.Longitude = item['X']
                obj.Latitude = item['Y']
                obj.Unique_Squirrel_ID = item['Unique Squirrel ID']
                obj.Shift = item['Shift']
                obj.Date = datetime.datetime.strptime(item['Date'],'%m%d%Y')
                obj.Age = item['Age']
                obj.Primary_Fur_Color = item['Primary Fur Color']
                obj.Location = item['Location']
                obj.Specific_Location = item['Specific Location']
                obj.Running = True if item['Running'].lower()=='true' else False
                obj.Chasing = True if item['Chasing'].lower()=='true' else False
                obj.Climbing = True if item['Climbing'].lower()=='true' else False
                obj.Eating = True if item['Eating'].lower()=='true' else False
                obj.Foraging = True if item['Foraging'].lower()=='true' else False
                obj.Other_Activities = item['Other Activities']
                obj.Kuks = True if item['Kuks'].lower()=='true' else False
                obj.Quaas = True if item['Quaas'].lower()=='true' else False
                obj.Moans = True if item['Moans'].lower()=='true' else False
                obj.Tail_Flags = True if item['Tail flags'].lower()=='true' else False
                obj.Tail_Twitches = True if item['Tail twitches'].lower()=='true' else False
                obj.Approaches = True if item['Approaches'].lower()=='true' else False
                obj.Indifferent = True if item['Indifferent'].lower()=='true' else False
                obj.Runs_From = True if item['Runs from'].lower()=='true' else False
                obj.save()

