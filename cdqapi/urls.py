from .views import inspire, test
from django.urls import path

urlpatterns = [
    path('inspire/', inspire, name="inspire"),
    path('test/', test, name="test")
]