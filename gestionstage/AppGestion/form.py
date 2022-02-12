from django.forms import *
from .models import *



class StagiaireForm (ModelForm):
    class Meta:
        model=Stagiaire
        fields="__all__"
        widgets = {
            'matricule': NumberInput(attrs={'class': 'input' }),
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
            'typeOr':Select(attrs={'class': 'input'})
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
        # exclude=['AnneeCourante']
        widgets={
            'Organisme':Select(attrs={'class': 'input'}),
            'Stage':Select(attrs={'class': 'input'}),
            'NivEtude':Select(attrs={'class': 'input' , 'id':'nivEtude'}),
            'Encadrant':Select(attrs={'class': 'input', 'id':'encadrant'}),
            'Promoteur':Select(attrs={'class': 'input', 'id':'promoteur'}),
            'Etudiant':SelectMultiple(attrs={'class':'input','style':'height:100px' , 'id':'select'}),
            'AnneeCourante':NumberInput(attrs={'class': 'input'}),
            'Sujet':Textarea(attrs={'class': 'input' ,'style':'height:60px', 'id':'sujet'})
        }
    