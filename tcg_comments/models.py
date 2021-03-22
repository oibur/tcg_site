from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    """A comment left by the user"""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
