from django.shortcuts import render,redirect
from .models import Event
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def events(request):
    events = Event.objects.all()
    context= {
        'events':events
    }
    return render(request, 'events.html', context)

def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form= BookingForm()
    dic_form={
        'form':form
    }
    return render(request, 'booking.html', dic_form)

def about(request):
    return render(request, 'about.html')