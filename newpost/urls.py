from django.urls import path
from .views import create_post, home

urlpatterns = [
    path('', home, name='home'),  # Home page URL
    path('create/', create_post, name='create_post'),
]
