from django.db import models
from Authors.models import Author

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Available', 'Available'), ('Borrowed', 'Borrowed')], default='Available')

    def __str__(self):
        return self.title