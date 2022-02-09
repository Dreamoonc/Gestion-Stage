from django.db.models import fields
from django.forms.widgets import *
import django_filters
from django_filters import *
from .models import *

NIV_ETUDE=(
(1,"CP1"),
(2,"CP2"),
(3,"CS1"),
(4,"CS2"),
(5,"CS3")
)
NIV_ETUDE_STAGE=(
(1,"CP1"),
(3,"CS1"),
(5,"CS3")
)

TYPE_ORGANISME=(
(1,"partenaire"),
(0,"nonPartenaire")
)

class StagaireFilter(django_filters.FilterSet):
    matricule=NumberFilter(label='',widget=NumberInput(attrs={'placeholder':'Matricule','class':'input_filter'}))
    NomStagiaire= CharFilter(label='',widget=TextInput(attrs={'placeholder':'Nom Stagiaire','class':'input_filter'}))
    PrenomStagiaire= CharFilter(label='',widget=TextInput(attrs={'placeholder':'Prenom Stagiaire','class':'input_filter'}))
    NivEtude=ChoiceFilter(choices=NIV_ETUDE,label='',widget=Select(attrs={'class':'input_filter'}))
    class  Meta :
       model = Stagiaire
       fields = '__all__'

    

class StageFilter(django_filters.FilterSet):
    NomStage= CharFilter(label='',widget=TextInput(attrs={'placeholder':'Nom Stage','class':'input_filter'}))
    NivEtude= ChoiceFilter(choices=NIV_ETUDE_STAGE,label='',widget=Select(attrs={'placeholder':'Nom Stage','class':'input_filter'}))
    Organisme =ModelChoiceFilter(queryset=Organisme.objects.all(),label='',widget=Select(attrs={'class':'input_filter'}))
    class  Meta :
       model = Stage
       fields = '__all__'

class PromoteurFilter(django_filters.FilterSet):
    NomPrenomPro= CharFilter(label='',widget=TextInput(attrs={'placeholder':'Nom Promoteur','class':'input_filter'}))
    Organisme=ModelChoiceFilter(queryset=Organisme.objects.all(),label='',widget=Select(attrs={'class':'input_filter'}))
    class  Meta :
       model = Promoteur
       fields = '__all__'

class EncaderantFilter(django_filters.FilterSet):
    NomPrenomEn=  CharFilter(label='',widget=TextInput(attrs={'placeholder':'Nom Encadrant','class':'input_filter'}))

    class  Meta :
       model = Encadrant
       fields = '__all__'

class OrganismeFilter(django_filters.FilterSet):
    NomOrganisme= CharFilter(label='',widget=TextInput(attrs={'placeholder':'Nom Encadrant','class':'input_filter'}))
    typeOr=ChoiceFilter(choices=TYPE_ORGANISME,label='',widget=Select(attrs={'class':'input_filter'}))

    class  Meta :
       model = Organisme
       fields = '__all__'

class Fiche_StageFilter(django_filters.FilterSet):
    NivEtude= ChoiceFilter(choices=NIV_ETUDE_STAGE,label='',widget=Select(attrs={'placeholder':'Nom Stage','class':'input_filter'}))
    Etudiant=NumberFilter(label='',widget=TextInput(attrs={'placeholder':'Matricule','class':'input_filter'}))
    Organisme=ModelChoiceFilter(queryset=Organisme.objects.all(),label='',widget=Select(attrs={'class':'input_filter'}))
    Stage=ModelChoiceFilter(queryset=Stage.objects.all(),label='',widget=Select(attrs={'class':'input_filter'}))
    Encadrant=ModelChoiceFilter(queryset=Encadrant.objects.all(),label='',widget=Select(attrs={'class':'input_filter'}))
    class  Meta :
       model = Fiche_Stage
       fields = '__all__'
       exclude =['Sujet','Promoteur','AnneeCourante']