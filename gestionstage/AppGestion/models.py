from django.db import models
import datetime

NIV_ETUDE_STAGE=(
(1,"CP1"),
(3,"CS1"),
(5,"CS3")
)
NIV_ETUDE=(
(1,"CP1"),
(2,"CP2"),
(3,"CS1"),
(4,"CS2"),
(5,"CS3")
)



class Stagiaire (models.Model):
    matricule= models.IntegerField(primary_key=True)
    NomStagiaire=models.CharField(max_length=15)
    PrenomStagiaire=models.CharField(max_length=30)
    NivEtude=models.IntegerField(choices=NIV_ETUDE)
    def __str__(self):
        return str(self.matricule)+' '+ self.NomStagiaire +' '+ self.PrenomStagiaire
    class Meta:
        ordering = ['NivEtude']


class Encadrant (models.Model):
    NomPrenomEn=models.CharField(max_length=40)
    def __str__(self):
        return self.NomPrenomEn 
    class Meta:
        ordering = ['NomPrenomEn']


class Organisme (models.Model):
    NomOrganisme= models.CharField(max_length=40,primary_key=True)
    typeOr=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.NomOrganisme 



class Promoteur (models.Model):
    NomPrenomPro=models.CharField(max_length=40)
    Organisme = models.ForeignKey("Organisme",on_delete=models.CASCADE)
    def __str__(self):
        return self.NomPrenomPro
    class Meta:
        ordering = ['NomPrenomPro']





class Stage (models.Model):
    NomStage = models.CharField(max_length=40)
    NivEtude= models.IntegerField(choices=NIV_ETUDE_STAGE)
    Organisme = models.ForeignKey("Organisme",on_delete=models.CASCADE)
    def __str__(self):
        return self.NomStage


class Fiche_Stage (models.Model):
    Groupe=models.IntegerField(default=0)
    Organisme=models.ForeignKey("Organisme",on_delete=models.CASCADE)
    Stage=models.ForeignKey("Stage",on_delete=models.CASCADE)
    NivEtude =models.IntegerField(choices=NIV_ETUDE_STAGE)
    Etudiant1=models.ForeignKey("stagiaire",on_delete=models.CASCADE,related_name='Fiche_Stage')
    Etudiant2=models.ForeignKey("stagiaire",on_delete=models.CASCADE,related_name='etudiants')
    Etudiant3=models.ForeignKey("stagiaire",on_delete=models.CASCADE)
    Encadrant=models.ForeignKey("Encadrant",on_delete=models.CASCADE)
    Promoteur=models.ForeignKey("Promoteur",on_delete=models.CASCADE)
    AnneeCourante=models.IntegerField(default=datetime.datetime.now().year)
    Sujet = models.CharField(max_length=60,unique=True,null=True,blank=True)

    class Meta:
        unique_together = (('Groupe','AnneeCourante'))

