from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Squirrel

def list_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }

    return render(request, 'sightings/list_squirrel.html', context)

def edit_squirrels(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=squirrel_id)
    context = {
            'squirrel_id':squirrel_id
    }
    return render(request, 'sightings/edit_squirrels.html', context)
