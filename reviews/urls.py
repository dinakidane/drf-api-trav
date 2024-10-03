from django.urls import path
from .views import ReviewListCreate

urlpatterns = [
    # Endpoint to list all reviews or create a new one
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
]