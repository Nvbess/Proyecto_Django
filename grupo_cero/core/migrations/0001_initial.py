# Generated by Django 5.0.4 on 2024-05-11 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_autor', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Arte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoarte', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Arte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_arte', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=1000)),
                ('valor', models.IntegerField(default=0)),
                ('imagen', models.ImageField(blank=True, default='', null=True, upload_to='arte')),
                ('habilitado', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.autor')),
                ('tipoarte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipo_arte')),
            ],
        ),
    ]
