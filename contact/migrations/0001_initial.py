# Generated by Django 4.1.1 on 2022-12-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('email', models.CharField(max_length=100, verbose_name='Correo electronico')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de enviado')),
            ],
            options={
                'verbose_name': 'contacto',
                'verbose_name_plural': 'contactos',
                'ordering': ['-created'],
            },
        ),
    ]
