from django.urls import path
from . import views

urlpatterns = [
    path('<str:relic_name>', views.relic_weapon, name='relic_weapon'),
]
