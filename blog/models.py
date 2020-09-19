from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    date = models.DateField()
    auhor = models.CharField(max_length=25)
