# Generated by Django 3.2.9 on 2022-02-09 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestion', '0026_alter_organisme_typeor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche_stage',
            name='Encadrant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppGestion.encadrant'),
        ),
        migrations.AlterField(
            model_name='fiche_stage',
            name='Promoteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppGestion.promoteur'),
        ),
    ]
