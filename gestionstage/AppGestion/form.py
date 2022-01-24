from django.forms import *
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
            'Encadrant':Select(attrs={'class': 'input'}),
            'Promoteur':Select(attrs={'class': 'input'}),
            'Etudiant':SelectMultiple(attrs={'class':'input','style':'height:100px' , 'id':'select'}),
            'AnneeCourante':NumberInput(attrs={'class': 'input'}),
            'Sujet':Textarea(attrs={'class': 'input' ,'style':'height:60px'})
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['Etudiant'].queryset=Stagiaire.objects.none()
        self.fields['Stage'].queryset=Stage.objects.none()
        self.fields['Promoteur'].queryset=Promoteur.objects.none()

        # if 'NivEtude' in self.data:
        #     try:
        #         NivEtude_id=int(self.data.get('NivEtude'))
        #         self.fields['Etudiant'].queryset=Stagiaire.objects.filter(NivEtude=NivEtude_id)
        #     except(ValueError,TypeError):
        #         pass
        # elif self.instance.pk:
        #     self.fields['Etudiant'].queryset=self.instance.NivEtude.Etudiant_set
        


        # if 'Organisme' in self.data:
        #     try:
        #         Organisme_id=int(self.data.get('Organisme'))
        #         self.fields['Promoteur'].queryset=Promoteur.objects.filter(Organisme=Organisme_id)
        #         self.fields['Stage'].queryset=Promoteur.objects.filter(Organisme=Organisme_id)
        #     except(ValueError,TypeError):
        #         pass
        # elif self.instance.pk:
        #     self.fields['Promoteur'].queryset=self.instance.Organisme.Promoteur_set
        #     self.fields['Stage'].queryset=self.instance.Organisme.Stage_set
