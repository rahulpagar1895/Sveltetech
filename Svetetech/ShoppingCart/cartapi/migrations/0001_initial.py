# Generated by Django 4.2.2 on 2023-06-15 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('details', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartapi.shoppingcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_quantity', models.PositiveIntegerField(default=1)),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartapi.shoppingcart')),
                ('shopping_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartapi.shoppingitems')),
            ],
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='shopping_items',
            field=models.ManyToManyField(through='cartapi.ShoppingCartItem', to='cartapi.shoppingitems'),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]