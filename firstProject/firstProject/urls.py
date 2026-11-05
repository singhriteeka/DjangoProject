
from django.contrib import admin
from django.urls import path

from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/',views.signup_view),

    path('login/',views.login_view),

    path('',views.landing_view)
]
