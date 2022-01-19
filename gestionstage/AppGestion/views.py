from django.shortcuts import redirect, render,HttpResponse
from django.contrib import  messages  
from django.http.response import HttpResponse
from .models import *
from .filters import *
from django.core.paginator import Paginator 
from AppGestion.form import *
# Create your views here.
def stagiaire (request):
    stagiaires=Stagiaire.objects.all()
    myFilter1 =StagaireFilter(request.GET, queryset=stagiaires)
    stagiaires=myFilter1.qs
    paginator= Paginator(stagiaires,5)
    page_number=request.GET.get('page')
    stagiaires=paginator.get_page(page_number)
    
    if request.method=="POST":
        formStagiaire =StagiaireForm(data=request.POST)
        if formStagiaire.is_valid():
            formStagiaire.save()
            return redirect("stagiaire")     
    else:
        formStagiaire=StagiaireForm
        
    return render(request,'stagiaire.html',{'stagiaire':stagiaires,'myFilter1':myFilter1,'formStagiaire':formStagiaire})
def formulaireStage(request ):
    ficheStage= Fiche_Stage.objects.all()
    if request.method=="POST":
        formficheStage =formFichStage(data=request.POST)
        if formficheStage.is_valid():
            formficheStage.save() 
            return redirect("formulaireStage")
    else:
        formficheStage=formFichStage
    return render(request,'formulaireStage.html',{'fiche':ficheStage ,'formFichStage':formficheStage})

def encadrant(request):
    encadrants=Encadrant.objects.all()
    enca=EncaderantFilter(request.GET, queryset=encadrants)
    encadrants=enca.qs
    paginator2= Paginator(encadrants,5)
    page_number=request.GET.get('page')
    encadrants=paginator2.get_page(page_number)
    if request.method=="POST":
        formEncadrant =EncadrantForm(data=request.POST)
        if formEncadrant.is_valid():
            formEncadrant.save()
            return redirect("encadrant")
    else:
        formEncadrant=EncadrantForm
    return render(request,'encadrant.html',{'encadrant':encadrants, 'enca':enca,'formEncadrant':formEncadrant})

def organisme(request):
    organismes=Organisme.objects.all()
    variable =OrganismeFilter(request.GET, queryset=organismes)
    organismes=variable.qs
    paginator5= Paginator(organismes,5)
    page_number=request.GET.get('page')
    organismes=paginator5.get_page(page_number)
    if request.method=="POST":
        formOrganisme =OrganismeForm(data=request.POST)
        if formOrganisme.is_valid():
            formOrganisme.save()
            return redirect("organisme")
    else:
        formOrganisme=OrganismeForm
    return render(request,'organisme.html',{'organisme':organismes,'formOrganisme':formOrganisme,'variable':variable})

def promoteur(request):
    promoteurs=Promoteur.objects.all()
    organismes=Organisme.objects.all()
    pro =PromoteurFilter(request.GET, queryset=promoteurs)
    promoteurs=pro.qs
    paginator4= Paginator(promoteurs,5)
    page_number=request.GET.get('page')
    promoteurs=paginator4.get_page(page_number)
    if request.method=="POST":
        formPromoteur =PromoteurForm(data=request.POST)
        if formPromoteur.is_valid():
            formPromoteur.save()
            return redirect("promoteur")
    else:
        formPromoteur=PromoteurForm
    return render(request,'promoteur.html',{'promoteur':promoteurs,'organismes':organismes,'pro':pro,'formPromoteur':formPromoteur})

def stage(request):
    stages=Stage.objects.all()
    organismes=Organisme.objects.all()
    sta= StageFilter(request.GET, queryset=stages)
    stages=sta.qs
    paginator3= Paginator(stages,5)
    page_number=request.GET.get('page')
    stages=paginator3.get_page(page_number)
    if request.method=="POST":
        formStage     =StageForm(data=request.POST)
        if formStage.is_valid():
            formStage.save()
            return redirect("stage")  
    else:
        formStage=StageForm

    return render(request,'stage.html',{'stage':stages,'organismes':organismes,'sta':sta,'formStage':formStage})

def login(request):
    return render(request,'login.html')
        

def delete_Stagaire (request,myid) :
    item = Stagiaire.objects.get(matricule =myid)
    item.delete()
    messages.info(request,'item delete seccely ')
    return redirect(stagiaire)

def delete_encaderant (request,myid) :
    item = Encadrant.objects.get(id =myid)
    item.delete()
    messages.info(request,'item delete seccely ')
    return redirect(encadrant)

def delete_organisme (request,myid) :
    item = Organisme.objects.get(NomOrganisme =myid)
    item.delete()
    messages.info(request,'item delete seccely ')
    return redirect(stagiaire)

def delete_promoteur (request,myid) :
    item = Promoteur.objects.get(id =myid)
    item.delete()
    messages.info(request,'item delete seccely ')
    return redirect(stagiaire)

def delete_stage (request,myid) :
    item = Stage.objects.get(id =myid)
    item.delete()
    messages.info(request,'item delete seccely ')
    return redirect(stagiaire)
    
def update_stagiaire (request,myid) :
    itemup = Stagiaire.objects.get(matricule =myid)
    form = StagiaireForm(request.POST,instance = itemup)
    if form.is_valid():
        form.save()
        messages.success(request,"Record Updated Successfully!!")
        return redirect(stagiaire)


def update_encadrant (request,myid) :
    itemup = Encadrant.objects.get(id =myid)
    form = EncadrantForm(request.POST,instance = itemup)
    if form.is_valid():
        form.save()
        messages.success(request,"Record Updated Successfully!!")
        return redirect(encadrant)


def update_promoteur (request,myid) :
    itemup = Promoteur.objects.get(id =myid)
    form = PromoteurForm(request.POST,instance = itemup)
    if form.is_valid():
        form.save()
        messages.success(request,"Record Updated Successfully!!")
        return redirect(promoteur)


def update_organisme (request,myid) :
    itemup = Organisme.objects.get(NomOrganisme =myid)
    form = OrganismeForm(request.POST,instance = itemup)
    if form.is_valid():
        form.save()
        messages.success(request,"Record Updated Successfully!!")
        return redirect(organisme)

def update_stage (request,myid) :
    itemup = Stage.objects.get(id =myid)
    form = StageForm(request.POST,instance = itemup)
    if form.is_valid():
        form.save()
        messages.success(request,"Record Updated Successfully!!")
        return redirect(stage)

