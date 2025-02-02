# Generated by Django 5.0.3 on 2024-04-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ImageField(upload_to='image')),
                ('price', models.IntegerField()),
                ('describtions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SpecialSoffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='image')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
