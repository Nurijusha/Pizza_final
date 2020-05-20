from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pizza_products.models import PizzaProduct


class Cook(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='user_images')
    urlfield = models.URLField()
    def __str__(self):
        return f'Повар {self.user.username}'

class Recommendation(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey('Cook', on_delete=models.CASCADE)
    pizza=models.ForeignKey(PizzaProduct,on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True, default=None)
    def __str__(self):
        return self.title
