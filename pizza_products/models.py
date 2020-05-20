from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class PizzaProduct(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='pizzas_images/', default="default image")
    class Meta:
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"
    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('pizza-detail', kwargs={'pk': self.pk})



class pizza_comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(PizzaProduct, on_delete=models.CASCADE, null=True, related_name='comments')
    text = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
