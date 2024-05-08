from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberList(generics.ListCreateAPIView):
    """
    List all subscribers, i.e. all instances of a user
    subscribing to another user'.
    Create a subscriber, i.e. subscribe to a user if logged in.
    Perform_create: associate the current logged in user with a subscriber.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SubscriberDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a subscriber
    No Update view, as we either subscribe or unsubscribe users
    Destroy a subscriber, i.e. unsubscribe someone if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
