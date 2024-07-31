from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class NotificationList(generics.ListAPIView):
    """
    List notifications for the logged-in user.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

class NotificationDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a notification (e.g., mark as read).
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
