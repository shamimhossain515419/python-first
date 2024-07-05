

from django.urls import path
from about.views import contact
from about.views import about

 
urlpatterns = [
    path('about1', contact),
    path('about2',about),
]
