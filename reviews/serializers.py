from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    # ReadOnlyField to show the owner's username instead of their ID
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        # Fields to include in the serialized data
        fields = ['id', 'owner', 'rating', 'content', 'created_at']