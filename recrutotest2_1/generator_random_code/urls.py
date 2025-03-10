from django.urls import path
from .views import generate_code

urlpatterns = [
    path('code', generate_code, name='generate_code'),
]
