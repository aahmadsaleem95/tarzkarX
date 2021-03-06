# Generated by Django 2.2.10 on 2021-10-30 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='media',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.Product'),
            preserve_default=False,
        ),
    ]
