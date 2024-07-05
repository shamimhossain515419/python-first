

from django.urls import path
from blogs.views import blog1
from blogs.views import blog2

 
urlpatterns = [
    path('blogs', blog1),
    path('blogs2/',blog2),
]
