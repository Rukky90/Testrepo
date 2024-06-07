from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()
    signature = models.CharField(max_length =140, default = "The Band")

     
    def __str__(self):
            return self.title
