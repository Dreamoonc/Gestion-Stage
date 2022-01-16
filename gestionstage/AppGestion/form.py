from django.forms import ModelForm ,NumberInput,TextInput,Select
from .models import *

class StagiaireForm (ModelForm):
    class Meta:
        model=Stagiaire
        fields="__all__"
        widgets = {
            'matricule': NumberInput(attrs={'class': 'form-control' }),
            'NomStagiaire': NumberInput(attrs={'class': 'form-control'}),
            'NomStagiaire': TextInput(attrs={'class': 'form-control'}),
            'PrenomStagiaire': TextInput(attrs={'class': 'form-control'}),
            'NivEtude':Select(attrs={'class': 'form-control'})
        }

class EncadrantForm (ModelForm):
    class Meta:
        model=Encadrant
        fields="__all__"
        widgets = {
            'NomPrenomEn': TextInput(attrs={'class': 'input' }),
        }
class OrganismeForm (ModelForm):
    class Meta:
        model=Organisme
        fields="__all__"
class PromoteurForm (ModelForm):
    class Meta:
        model=Promoteur
        fields="__all__"
class StageForm (ModelForm):
    class Meta:
        model=Stage
        fields="__all__"

class formFichStage (ModelForm):
    class Meta :
        model=Fiche_Stage
        fields="__all__"
        exclude =['Groupe','matricule','Sujet']