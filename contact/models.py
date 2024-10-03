from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    """
    Model to handle user contact inquiries.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')  # User who submitted
    name = models.CharField(max_length=255)  # User's name
    email = models.EmailField()  # User's email
    message = models.TextField()  # Inquiry or complaint
    created_at = models.DateTimeField(auto_now_add=True)  # Date created

    class Meta:
        ordering = ['-created_at']  # Sort by newest first

    def __str__(self):
        return f'Contact from {self.name}'  # Display name in admin