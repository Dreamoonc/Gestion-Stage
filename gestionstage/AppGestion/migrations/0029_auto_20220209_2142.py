# Generated by Django 3.2.9 on 2022-02-09 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestion', '0028_alter_fiche_stage_sujet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche_stage',
            name='Encadrant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppGestion.encadrant'),
        ),
        migrations.AlterField(
            model_name='fiche_stage',
            name='Promoteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppGestion.promoteur'),
        ),
    ]
