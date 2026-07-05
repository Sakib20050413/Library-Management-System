from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=200)
    contact_details = models.TextField()

    def __str__(self):
        return self.name