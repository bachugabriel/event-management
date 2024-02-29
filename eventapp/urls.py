from django.urls import path
from eventapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('events',views.events,name='events'),
    path('booking',views.booking,name='booking'),
    path('about',views.about,name='about'),
]