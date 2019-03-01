from django.shortcuts import render, redirect
from .forms import TimeCardForm
from .models import TimeCard
from django.http import HttpResponse
# Create your views here.




#index page function

def index(request):
    allTimeEntries = TimeCard.objects.all()
    context = {
        'allTimeEntries': allTimeEntries,

    }
    return render(request, 'teachTimeApp/index.html', context)

# function for the form page to make a new entry

def newTimecard(request):
    timeForm = TimeCardForm(request.POST or None)
    if timeForm.is_valid():
        timeForm.save()
        return redirect('index')

    return render(request, 'teachTimeApp/timeform.html', {'timeForm': timeForm})

# function for name redirect, showes all entries by the name selected

def nameLink(request):
    return render(request, 'teachTimeApp/timecardDetails.html')