# Generated by Django 3.0 on 2019-12-19 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0002_auto_20191219_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('similar_products', models.ManyToManyField(related_name='_product_similar_products_+', to='many_to_many.Product')),
            ],
        ),
    ]
