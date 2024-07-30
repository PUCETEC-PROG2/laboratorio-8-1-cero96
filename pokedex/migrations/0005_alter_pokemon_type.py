# Generated by Django 4.2 on 2024-07-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0004_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('E', 'Eléctrico'), ('A', 'Agua'), ('F', 'Fuego'), ('T', 'Tierra'), ('P', 'Planta')], max_length=30),
        ),
    ]
