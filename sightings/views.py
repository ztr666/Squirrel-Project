from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import SquirrelForm
from django.db.models import Max, Min, Count

from .models import Squirrel

def list_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }

    return render(request, 'sightings/list_squirrel.html', context)

def detail(request, squirrel_id):
    squirrels = Squirrel.objects.get(Unique_Squirrel_ID=squirrel_id)
    context = {
            'squirrels': squirrels,
    }
    return render(request, 'sightings/detail.html', context)

def edit_squirrels(request, squirrel_id):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=squirrel_id)
    if request.method=='POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm(instance=squirrel)
    return render(request, 'sightings/edit_squirrels.html', {'form': form})

def add_squirrels(request):
    if request.method=='POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SquirrelForm()
    return render(request, 'sightings/add_squirrel.html', {'form': form})

def stats(request):
    squirrels = Squirrel.objects.all()
    num_of_squirrels = len(squirrels)
    latitude = squirrels.aggregate(minimum=Min('Latitude'),maximum=Max('Latitude'))
    longitude = squirrels.aggregate(minimum=Min('Longitude'),maximum=Max('Longitude'))
    primary_fur_color =list(squirrels.values_list('Primary_Fur_Color').annotate(Count('Primary_Fur_Color')))
    shift = list(squirrels.values_list('Shift').annotate(Count('Shift')))
    age = list(squirrels.values_list('Age').annotate(Count('Age')))
    context = {
            'num_of_squirrels': num_of_squirrels,
            'latitude': latitude,
            'longitude': longitude,
            'primary_fur_color': primary_fur_color,
            'shift': shift,
            'age': age,
    }
    return render(request, 'sightings/stats.html', context)
