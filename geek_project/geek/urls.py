from django.urls import path
from geek.views import squad_power

urlpatterns = [
    path("", squad_power, name="home")
]
