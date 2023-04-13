from django.urls import path
from .views import my_view, test_view

urlpatterns = [
    path('', my_view, name='myview'),
    path('test/', test_view, name='test'),
]