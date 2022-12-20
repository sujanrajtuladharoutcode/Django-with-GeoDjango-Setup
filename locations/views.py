from django.shortcuts import render, redirect
from .forms import LocationForm
from .models import Location


def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('locations')
    else:
        form = LocationForm()
    return render(request, 'locations/add.html', {'form': form})


def list_locations(request):
    locations = Location.objects.all()
    return render(request, 'locations/list.html', {'locations': locations})