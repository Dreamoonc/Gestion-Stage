from django.db.models import fields
import django_filters
from django_filters import CharFilter
from .models import *

class StagaireFilter(django_filters.FilterSet):
    NomStagiaire= CharFilter(field_name='NomStagiaire' , lookup_expr='icontains')
    PrenomStagiaire= CharFilter(field_name='PrenomStagiaire' , lookup_expr='icontains' )
    class  Meta :
       model = Stagiaire
       fields = '__all__'

class StageFilter(django_filters.FilterSet):
    NomStage= CharFilter(field_name='NomStage' , lookup_expr='icontains' )
    class  Meta :
       model = Stage
       fields = '__all__'

class PromoteurFilter(django_filters.FilterSet):
    NomPrenomPro= CharFilter(field_name='NomPrenomPro' , lookup_expr='icontains' )
    
    class  Meta :
       model = Promoteur
       fields = '__all__'

class EncaderantFilter(django_filters.FilterSet):
    NomPrenomEn= CharFilter(field_name='NomPrenomEn' , lookup_expr='icontains' )

    class  Meta :
       model = Encadrant
       fields = '__all__'

class OrganismeFilter(django_filters.FilterSet):
    NomOrganisme= CharFilter(field_name='NomOrganisme' , lookup_expr='icontains' )

    class  Meta :
       model = Organisme
       fields = '__all__'

class Fiche_StageFilter(django_filters.FilterSet):
  
    class  Meta :
       model = Fiche_Stage
       fields = '__all__'
       exclude =['AnneeCourante','Sujet','Promoteur','Stage','Etudiant']