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
    
]
