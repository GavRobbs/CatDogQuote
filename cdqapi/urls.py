from .views import inspire
from django.urls import path

urlpatterns = [
    path('inspire/', inspire, name="inspire"),
]