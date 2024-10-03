from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    # Foreign key linking the review to the user who posted it
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Rating field with choices from 1 to 5
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    
    # Field for the review text content
    content = models.TextField()
    
    # Automatically set the created_at field to the current timestamp when a review is created
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Order reviews by creation date, with the newest first
        ordering = ['-created_at']

    def __str__(self):
        # String representation of the review
        return f'Review by {self.owner.username} - Rating: {self.rating}'
