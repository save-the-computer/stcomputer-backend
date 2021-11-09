# Generated by Django 3.2.8 on 2021-11-09 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_downloadthumbnailqueuedproductspec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.productspec'),
        ),
        migrations.AlterField(
            model_name='product',
            name='variant',
            field=models.CharField(max_length=200, null=True),
        ),
    ]