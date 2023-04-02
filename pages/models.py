from django.db import models

# Create your models here.

class Post(models.Model):
    LOW = 'L'
    MEDIUM = 'M'
    HIGH = 'H'
    PRIORITY = [(LOW, 'Low'), (MEDIUM, 'Medium'), (HIGH, 'High')]
    name         = models.CharField(max_length=60)
    price        = models.IntegerField()
    description  = models.TextField(max_length=1000)
    photo        = models.TextField(max_length=1000)
    priority     = models.CharField(max_length=6, choices=PRIORITY)

    def __str__(self):
        return self.name
    