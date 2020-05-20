from django.db import models

class Cook(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

class Discounts(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Cook', related_name='discounts', on_delete=models.CASCADE)
    period = models.IntegerField()
    def __str__(self):
        return self.title
