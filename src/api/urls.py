from django.urls import path

from .views import index

urlpatterns = [
    path("lancamentos", index, name="index"),
]