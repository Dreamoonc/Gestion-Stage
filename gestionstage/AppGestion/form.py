from django.forms import ModelForm ,NumberInput,TextInput,Select
from .models import *

class StagiaireForm (ModelForm):
    class Meta:
        model=Stagiaire
        fields="__all__"
        widgets = {
            'matricule': NumberInput(attrs={'class': 'input' }),
            'NomStagiaire': NumberInput(attrs={'class': 'input'}),
            'NomStagiaire': TextInput(attrs={'class': 'input'}),
            'PrenomStagiaire': TextInput(attrs={'class': 'input'}),
            'NivEtude':Select(attrs={'class': 'input'})
        }

class EncadrantForm (ModelForm):
    class Meta:
        model=Encadrant
        fields="__all__"
        widgets = {
            'NomPrenomEn': TextInput(attrs={'class': 'input'}),
        }
class OrganismeForm (ModelForm):
    class Meta:
        model=Organisme
        fields="__all__"
        widgets={
            'NomOrganisme':TextInput(attrs={'class': 'input'}),
            'typeOr':TextInput(attrs={'class': 'input'})
        }
class PromoteurForm (ModelForm):
    class Meta:
        model=Promoteur
        fields="__all__"
        widgets={
            'NomPrenomPro':TextInput(attrs={'class': 'input'}),
            'Organisme':Select(attrs={'class': 'input'})
        }
class StageForm (ModelForm):
    class Meta:
        model=Stage
        fields="__all__"
        widgets={
            'NomStage':TextInput(attrs={'class': 'input'}),
            'NivEtude':Select(attrs={'class': 'input'}),
            'Organisme':Select(attrs={'class': 'input'})
        }

class formFichStage (ModelForm):
    class Meta :
        model=Fiche_Stage
        fields="__all__"
        exclude =['AnneeCourante']
        widgets={
            'Groupe':NumberInput(attrs={'class': 'input'}),
            'Organisme':Select(attrs={'class': 'input'}),
            'Stage':Select(attrs={'class': 'input'}),
            'NivEtude':Select(attrs={'class': 'input'}),
            'Etudiant1':Select(attrs={'class': 'input'}),
            'Etudiant2':Select(attrs={'class': 'input'}),
            'Etudiant3':Select(attrs={'class': 'input'}),
            'Encadrant':Select(attrs={'class': 'input'}),
            'Promoteur':Select(attrs={'class': 'input'}),
            'AnneeCourante':NumberInput(attrs={'class': 'input'}),
            'Sujet':TextInput(attrs={'class': 'input'})
        }