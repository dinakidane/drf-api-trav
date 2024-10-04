from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsOwnerOrReadOnly

class ReviewListCreate(generics.ListCreateAPIView):
    """
    View to list all reviews or create a new review if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Only authenticated users can create reviews
    serializer_class = ReviewSerializer  # Specify the serializer to use
    queryset = Review.objects.all()  # Get all reviews

    def perform_create(self, serializer):
        # Associate the current logged in user with the review being created
        serializer.save(owner=self.request.user)

class ReviewDetail(generics.RetrieveDestroyAPIView):
    """
    View to retrieve or delete a specific review.
    Only the owner of the review can delete it.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # Restrict delete to the owner
    serializer_class = ReviewSerializer  # Specify the serializer to use
    queryset = Review.objects.all()  # Get all reviews (filtered by ID in the URL)