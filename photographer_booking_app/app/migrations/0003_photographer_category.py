# Generated by Django 4.2.13 on 2024-06-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='Category',
            field=models.CharField(blank=True, choices=[('Adventure Photography', 'Adventure Photography'), ('Aerial Photography', 'Aerial Photography'), ('Astro Photography', 'Astro Photography'), ('Automotive Photography', 'Automotive Photography'), ('Commercial Photography', 'Commercial Photography'), ('Documentary Photography', 'Documentary Photography'), ('Event Photography', 'Event Photography'), ('Fashion Photography', 'Fashion Photography'), ('Fine Art Photography', 'Fine Art Photography'), ('Food Photography', 'Food Photography'), ('Industrial Photography', 'Industrial Photography'), ('Landscape Photography', 'Landscape Photography'), ('Medical Photography', 'Medical Photography'), ('Pet Photography', 'Pet Photography'), ('Photojournalist', 'Photojournalist'), ('Portrait Photography', 'Portrait Photography'), ('Product Photography', 'Product Photography'), ('Real Estate Photography', 'Real Estate Photography'), ('Scientific Photography', 'Scientific Photography'), ('Sports Photography', 'Sports Photography'), ('Stock Photography', 'Stock Photography'), ('Street Photography', 'Street Photography'), ('Travel Photography', 'Travel Photography'), ('War Photography', 'War Photography'), ('Wedding Photography', 'Wedding Photography'), ('Wildlife Photography', 'Wildlife Photography')], max_length=1000, null=True, verbose_name='Genre'),
        ),
    ]
