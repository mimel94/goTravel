# Generated by Django 2.0 on 2021-09-09 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0002_auto_20210909_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='album_url',
            field=models.ImageField(null=True, upload_to='sitios'),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=254, verbose_name='Ubicacion'),
        ),
    ]
