from django.urls import path
from .views import ContactCreate

urlpatterns = [
    path('contact/', ContactCreate.as_view(), name='contact-create'),  # URL for contact form
]