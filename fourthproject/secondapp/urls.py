from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.index_view, name='test'),
]
