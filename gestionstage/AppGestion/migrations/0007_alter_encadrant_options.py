# Generated by Django 3.2.9 on 2021-12-29 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestion', '0006_auto_20211229_2331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='encadrant',
            options={'ordering': ['NomPrenomEn']},
        ),
    ]
