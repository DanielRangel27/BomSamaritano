# Generated by Django 4.0.4 on 2022-04-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_familia_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='tempo',
            field=models.DateField(verbose_name='Tempo de Rua'),
        ),
    ]