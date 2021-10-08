# Generated by Django 3.2.8 on 2021-10-07 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('variant', models.CharField(max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('stock_state', models.CharField(max_length=30)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level1', models.CharField(max_length=100)),
                ('level2', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('name', 'level1', 'level2')},
            },
        ),
        migrations.CreateModel(
            name='WritePointQueuedProduct',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpec',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
                ('registration_date', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productcategory')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productspec'),
        ),
    ]