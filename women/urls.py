from django.urls import path
from women.views import index

urlpatterns = [
    path('', index),
]
