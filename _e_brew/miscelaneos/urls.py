from django.urls import path
from .views import quiero_una

urlpatterns = [
    path('iwant/', quiero_una)    
]
