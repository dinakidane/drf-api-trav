from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status

class ContactCreate(generics.CreateAPIView):
    """
    View for creating contact inquiries.
    """
    serializer_class = ContactSerializer  # Use the ContactSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can submit

    def perform_create(self, serializer):
        """
        Save the contact with the logged-in user.
        """
        serializer.save(owner=self.request.user)  # Link contact to user

    def create(self, request, *args, **kwargs):
        """
        Override to send a success message after creation.
        """
        serializer = self.get_serializer(data=request.data)  # Get serializer with data
        serializer.is_valid(raise_exception=True)  # Validate data
        self.perform_create(serializer)  # Save the contact
        return Response({"message": "Your enquiry/complaint has been sent."}, status=status.HTTP_201_CREATED)  # Success message
