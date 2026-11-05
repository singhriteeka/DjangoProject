from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index_view),
    path('addpyth/<int:first>/<int:second>/',views.add),
]
