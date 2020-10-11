from django.http import HttpResponse
from django.shortcuts import render


def list_squirrels(request):
    return render(request, 'sightings/list_squirrel.html', {})
