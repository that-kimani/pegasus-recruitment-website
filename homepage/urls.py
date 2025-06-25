from django.urls import path
from . import views

# URLS here
urlpatterns = [
    path('' , views.serve_homepage , name='Serve Homepage'),
]