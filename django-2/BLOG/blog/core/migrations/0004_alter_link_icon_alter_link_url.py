# Generated by Django 4.1.7 on 2023-03-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_about_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Icono'),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(blank=True, max_length=350, null=True, verbose_name='Enlace'),
        ),
    ]