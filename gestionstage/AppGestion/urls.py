from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.login,name='login'),
    path('formulaireStage/',views.formulaireStage,name='formulaireStage'),
    path('stagiaire/',views.stagiaire,name='stagiaire'),
    path('encadrant/',views.encadrant,name='encadrant'),
    path('stage/',views.stage,name='stage'),
    path('organisme/',views.organisme,name='organisme'),
    path('promoteur/',views.promoteur,name='promoteur'),
    path('delete_stagaire/<str:myid>/',delete_Stagaire,name='delete_Stagaire'),
    path('delete_encaderant/<int:myid>/',delete_encaderant,name='delete_encaderant'),
    path('delete_organisme/<str:myid>/',delete_organisme,name='delete_organisme'),
    path('delete_promoteur/<int:myid>/',delete_promoteur,name='delete_promoteur'),
    path('delete_stage/<int:myid>/',delete_stage,name='delete_stage'),
    path('Update_Stagiaire/<str:myid>/',update_stagiaire,name='Update_Stagiaire'),
    path('Update_Encadrant/<int:myid>/',update_encadrant,name='Update_Encadrant'),
    path('Update_Promoteur/<int:myid>/',update_promoteur,name='Update_Promoteur'),
    path('Update_Organisme/<str:myid>/',update_organisme,name='Update_Organisme'),
    path('Update_Stage/<int:myid>/',update_stage,name='Update_Stage'),
    path('tableFormulaireStage/',tableFormulaireStage,name='tableFormulaireStage'),
    path('delete_tableform/<str:myid>/',delete_tableform,name='delete_tableform'),
    
    path('ajax/load-Etudiant',views.load_Etudiant,name='ajax_load_Etudiant'),
    path('ajax/load-Promoteur',views.load_Promoteur,name='ajax_load_Promoteur'),
    path('ajax/load-Stage',views.load_Stage,name='ajax_load_Stage'),
    path('ajax/load-StageNiv',views.load_StageNiv,name='ajax_load_StageNiv'),
    


    path('Statistiques/<int:year>/',get_Chart,name='pfe_chart'),
    path('Statistiques/2022/',get_Chart,name='Statistiques'),
   
    
]
