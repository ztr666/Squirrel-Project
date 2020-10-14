from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import SquirrelForm

from .models import Squirrel

def list_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }

    return render(request, 'sightings/list_squirrel.html', context)

def edit_squirrels(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=squirrel_id)
    if request.method=='POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(request.POST.get('next', '/'))
            #return render(request,'/sighting/', {'squirrel':squirrel})
    else:
        form = SquirrelForm(instance=squirrel)
    return render(request, 'sightings/edit_squirrels.html', {'form': form})
