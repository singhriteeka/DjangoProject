from django.urls import path, include
from . import views
from firstapp import urls as first_urls
from secondapp import urls as second_urls
urlpatterns = [
    path('first/', include(first_urls)),
    path('second/', include(second_urls)),
    
]

