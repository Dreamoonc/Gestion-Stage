# Generated by Django 3.2.9 on 2022-02-08 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestion', '0022_auto_20220125_0017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fiche_stage',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='fiche_stage',
            name='NivEtude',
            field=models.IntegerField(choices=[('CP1', 'CP1'), ('CS1', 'CS1'), ('CS3', 'CS3')]),
        ),
        migrations.AlterField(
            model_name='organisme',
            name='typeOr',
            field=models.IntegerField(choices=[('partenaire', 'partenaire'), ('non partenaire', 'non partenaire')]),
        ),
        migrations.AlterField(
            model_name='stage',
            name='NivEtude',
            field=models.IntegerField(choices=[('CP1', 'CP1'), ('CS1', 'CS1'), ('CS3', 'CS3')]),
        ),
        migrations.AlterField(
            model_name='stagiaire',
            name='NivEtude',
            field=models.IntegerField(choices=[('CP1', 'CP1'), ('CP2', 'CP2'), ('CS1', 'CS1'), ('CS2', 'CS2'), ('CS3', 'CS3')]),
        ),
    ]
