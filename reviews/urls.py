from django.urls import path
from .views import ReviewListCreate, ReviewDetail

urlpatterns = [
    # Endpoint to list all reviews or create a new one
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'), 
]