# Generated by Django 3.2.9 on 2022-01-24 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestion', '0021_remove_fiche_stage_etudiant1_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stage',
            options={'ordering': ['NomStage']},
        ),
        migrations.AlterField(
            model_name='organisme',
            name='typeOr',
            field=models.IntegerField(choices=[(1, 'partenaire'), (0, 'non partenaire')], default=0),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='fiche_stage',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='fiche_stage',
            name='Groupe',
        ),
    ]
