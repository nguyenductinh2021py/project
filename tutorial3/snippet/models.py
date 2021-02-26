from django.db import models

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    