from django.db import models

# Create your models here.

# Model for the data received from advanced guidance submissions.
class Submission(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    topic = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullName} - {self.topic}"
