# Generated by Django 4.0.4 on 2022-05-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_tipo_2_pokedex_tipo_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('sobrenome', models.CharField(max_length=35)),
                ('senha', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
