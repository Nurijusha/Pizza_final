# Generated by Django 3.0.2 on 2020-02-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_products', '0003_pizzaproduct_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzaproduct',
            name='image',
            field=models.ImageField(default='default image', upload_to='pizzas_images/'),
        ),
        migrations.DeleteModel(
            name='PizzaProductImage',
        ),
    ]