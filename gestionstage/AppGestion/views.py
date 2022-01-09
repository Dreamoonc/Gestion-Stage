from django.shortcuts import redirect, render,HttpResponse
from django.contrib import  messages  
from django.http.response import HttpResponse
from .models import *
from .filters import *
from django.core.paginator import Paginator 
# Create your views here.
def index (request):
    stagiaires=Stagiaire.objects.all()
    encadrants=Encadrant.objects.all()
    organismes=Organisme.objects.all()
    promoteurs=Promoteur.objects.all()
    stages=Stage.objects.all()
    fiche_Stages=Fiche_Stage.objects.all()
    myFilter1 =StagaireFilter(request.GET, queryset=stagiaires)
    stagiaires=myFilter1.qs
    variable =OrganismeFilter(request.GET, queryset=organismes)
    organismes=variable.qs
    sta= StageFilter(request.GET, queryset=stages)
    stages=sta.qs
    enca=EncaderantFilter(request.GET, queryset=encadrants)
    encadrants=enca.qs
    pro =PromoteurFilter(request.GET, queryset=promoteurs)
    promoteurs=pro.qs
    paginator= Paginator(stagiaires,6)
    page_number=request.GET.get('page')
    stagiaires=paginator.get_page(page_number)
    paginator2= Paginator(encadrants,6)
    page_number=request.GET.get('page')
    encadrants=paginator2.get_page(page_number)
    paginator3= Paginator(stages,6)
    page_number=request.GET.get('page')
    stages=paginator3.get_page(page_number)
    paginator4= Paginator(promoteurs,6)
    page_number=request.GET.get('page')
    promoteurs=paginator4.get_page(page_number)
    paginator5= Paginator(organismes,6)
    page_number=request.GET.get('page')
    organismes=paginator5.get_page(page_number)
    return render(request,'index.html',{'stagiaire':stagiaires,'encadrant':encadrants
                   ,'organisme':organismes,'promoteur':promoteurs,'stage':stages,'ficheS':fiche_Stages
                   ,'myFilter1':myFilter1 , 'variable':variable , 'sta': sta , 'enca':enca 
                   ,'pro':pro})

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
    


