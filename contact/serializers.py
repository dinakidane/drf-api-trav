from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for validating contact data.
    """
    class Meta:
        model = Contact  # Specify the model
        fields = ['id', 'name', 'email', 'message', 'created_at']  # Fields to include

    def create(self, validated_data):
        """
        Create a new Contact instance.
        """
        return Contact.objects.create(**validated_data)  # Save the instance