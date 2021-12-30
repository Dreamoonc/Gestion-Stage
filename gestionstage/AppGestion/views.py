from django.shortcuts import render
from .models import *
# Create your views here.
def index (request):
    stagiaires=Stagiaire.objects.all()
    encadrants=Encadrant.objects.all()
    organismes=Organisme.objects.all()
    promoteurs=Promoteur.objects.all()
    stages=Stage.objects.all()
    fiche_Stages=Fiche_Stage.objects.all()
    
    return render(request,'index.html',{'stagiaire':stagiaires,'encadrant':encadrants
                   ,'organisme':organismes,'promoteur':promoteurs,'stage':stages,'ficheS':fiche_Stages})