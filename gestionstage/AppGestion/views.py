from django.shortcuts import redirect, render,HttpResponse
from django.contrib import  messages  
from django.http.response import HttpResponse
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

def delete_Stagaire (request,myid) :
    item = Stagiaire.objects.get(matricule =myid)
    item.delete()
    messages.info(request,'item delete seccely ')
    return redirect(index)

def delete_encaderant (request,myid) :
    item = Encadrant.objects.get(id =myid)
    item.delete()
    messages.info(request,'item delete seccely ')
    return redirect(index)

def delete_organisme (request,myid) :
    item = Organisme.objects.get(NomOrganisme =myid)
    item.delete()
    messages.info(request,'item delete seccely ')
    return redirect(index)

def delete_promoteur (request,myid) :
    item = Promoteur.objects.get(id =myid)
    item.delete()
    messages.info(request,'item delete seccely ')
    return redirect(index)

def delete_stage (request,myid) :
    item = Stage.objects.get(id =myid)
    item.delete()
    messages.info(request,'item delete seccely ')
    return redirect(index)
    


