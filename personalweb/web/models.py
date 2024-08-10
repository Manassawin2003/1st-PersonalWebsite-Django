from django.db import models  # Make sure to import models
from django.contrib.auth.models import User  # Import User model if you're using it

class Profile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    story = models.TextField()
    interestspecial = models.TextField()
    projectdevelop = models.TextField()
    tooldevelop = models.CharField(max_length=255)

    def __str__(self):
        return self.name
