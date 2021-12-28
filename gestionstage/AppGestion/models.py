from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Stagiaire (models.Model):
    matricule= models.CharField(max_length=15,primary_key=True)
    NomStagiaire=models.CharField(max_length=15)
    PrenomStagiaire=models.CharField(max_length=30)
    NivEtude=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],)


class Encadrant (models.Model):
    NomPrenomEn=models.CharField(max_length=40)


class OrganismedAccueil (models.Model):
    NomOrganisme= models.CharField(max_length=40,primary_key=True)
    typeOr=models.CharField(max_length=20,null=True)


class Promoteur (models.Model):
    NomPrenomPro=models.CharField(max_length=40)
    Organisme = models.ForeignKey("OrganismedAccueil",on_delete=models.CASCADE)


class TypeStage (models.Model):
    NomType= models.CharField(max_length=3,primary_key=True)
    NivEtude=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],)
    periode=models.CharField(max_length=30)


class Stage (models.Model):
    NomStage = models.CharField(max_length=40)
    Sujet = models.CharField(max_length=60)
    TypeStage= models.ForeignKey("TypeStage",on_delete=models.CASCADE)
    Organisme = models.ForeignKey("OrganismedAccueil",on_delete=models.CASCADE)


class Faire_Stage (models.Model):
    Organisme=models.ForeignKey("OrganismedAccueil",on_delete=models.CASCADE)
    Stage=models.ForeignKey("Stage",on_delete=models.CASCADE)
    matricule=models.ForeignKey("Stagiaire",on_delete=models.CASCADE)
    Encadrant=models.ForeignKey("Encadrant",on_delete=models.CASCADE)
    Promoteur=models.ForeignKey("Promoteur",on_delete=models.CASCADE)
    NivEtude=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],)
    AnneeCourante=models.IntegerField(default=datetime.datetime.now().year)
    Groupe=models.IntegerField()

    class Meta:
        unique_together = (('matricule','NivEtude','AnneeCourante'),)