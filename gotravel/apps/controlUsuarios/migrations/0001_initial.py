# Generated by Django 2.0 on 2021-08-23 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electronico')),
                ('tipo_documento', models.CharField(choices=[('ti', 'Tarjeta de identidad'), ('cc', 'Cedula de ciudadania')], max_length=50, null=True, verbose_name='Tipo de documento')),
                ('numero_documento', models.IntegerField(unique=True, verbose_name='Numero de documento')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('edad', models.IntegerField(null=True, verbose_name='Edad')),
                ('ocupacion', models.CharField(max_length=50, null=True)),
                ('admin', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
