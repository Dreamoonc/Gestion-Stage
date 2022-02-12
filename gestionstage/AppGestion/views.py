from django.shortcuts import redirect, render,HttpResponse
from django.contrib import  messages  
from django.http.response import HttpResponse
from .models import *
from .filters import *
from django.db.models import F
from django.core.paginator import Paginator 
from AppGestion.form import *
from django.db.models import Count
from django.http import JsonResponse
from json import dumps
from itertools import count


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



def formulaireStage(request):
    ficheStage= Fiche_Stage.objects.all()
    if request.method=="POST":
        formficheStage =formFichStage(data=request.POST)
        print(formficheStage)
        if formficheStage.is_valid():
            formficheStage.save()   
            return redirect("formulaireStage")
    else:
        formficheStage=formFichStage

    return render(request,'formulaireStage.html',{'fiche':ficheStage ,'formficheStage':formficheStage})

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


def tableFormulaireStage (request):
    tab=Fiche_Stage.objects.all()
    myFilter1 =Fiche_StageFilter(request.GET, queryset=tab)
    tab=myFilter1.qs
    paginator= Paginator(tab,3)
    page_number=request.GET.get('page')
    tab=paginator.get_page(page_number)
    return render(request,'tableFormulaireStage.html',{'form':tab,'myFilter1':myFilter1})
    

def login(request):
    return render(request,'login.html')
        

def delete_Stagaire (request,myid) :
    item = Stagiaire.objects.get(matricule =myid)
    item.delete()
    messages.info(request,'Stagiaire supprimé')
    return redirect(stagiaire)

def delete_encaderant (request,myid) :
    item = Encadrant.objects.get(id =myid)
    item.delete()
    messages.info(request,'Encadrant supprimé')
    return redirect(encadrant)

def delete_organisme (request,myid) :
    item = Organisme.objects.get(NomOrganisme =myid)
    item.delete()
    messages.info(request,'Organisme supprimé')
    return redirect(organisme)

def delete_promoteur (request,myid) :
    item = Promoteur.objects.get(id =myid)
    item.delete()
    messages.info(request,'Promoteur supprimé')
    return redirect(promoteur)

def delete_stage (request,myid) :
    item = Stage.objects.get(id =myid)
    item.delete()
    messages.info(request,'Stage supprimé')
    return redirect(stage)
    
def update_stagiaire (request,myid) :
    itemup = Stagiaire.objects.get(matricule =myid)
    form = StagiaireForm(request.POST,instance = itemup)
    if form.is_valid():
        form.save()
        messages.success(request,"Stagiaire modifié")
        return redirect(stagiaire)


def update_encadrant (request,myid) :
    itemup = Encadrant.objects.get(id =myid)
    form = EncadrantForm(request.POST,instance = itemup)
    if form.is_valid():
        form.save()
        messages.success(request,"Encadrant modifié")
        return redirect(encadrant)


def update_promoteur (request,myid) :
    itemup = Promoteur.objects.get(id =myid)
    form = PromoteurForm(request.POST,instance = itemup)
    if form.is_valid():
        form.save()
        messages.success(request,"Promoteur modifié")
        return redirect(promoteur)


def update_organisme (request,myid) :
    itemup = Organisme.objects.get(NomOrganisme =myid)
    form = OrganismeForm(request.POST,instance = itemup)
    if form.is_valid():
        form.save()
        messages.success(request,"Organisme modifié")
        return redirect(organisme)

def update_stage (request,myid) :
    itemup = Stage.objects.get(id =myid)
    form = StageForm(request.POST,instance = itemup)
    if form.is_valid():
        form.save()
        messages.success(request,"Stage modifié")
        return redirect(stage)


def delete_tableform(request,myid) :
    item = Fiche_Stage.objects.get(id =myid)
    item.delete()
    messages.info(request,'Fiche supprimée')
    return redirect(tableFormulaireStage)

def load_Etudiant(request):
    NivEtude_id=request.GET.get('NivEtude')
    Etudiants=Stagiaire.objects.filter(NivEtude=NivEtude_id)
    return render(request,'chained_dropdowns/Etudiant_dropdown_list_options.html',{'Etudiants':Etudiants})


def load_Promoteur(request):
    Organisme_id=request.GET.get('Organisme')
    Promoteurs=Promoteur.objects.filter(Organisme=Organisme_id)
    return render(request,'chained_dropdowns/Promoteur_dropdown_list_options.html',{'Promoteurs':Promoteurs})

def load_Stage(request):
    Organisme_id=request.GET.get('Organisme')
    Stages=Stage.objects.filter(Organisme=Organisme_id)
    return render(request,'chained_dropdowns/Stage_dropdown_list_options.html',{'Stages':Stages})

def load_StageNiv(request):
    NivEtude_id=request.GET.get('NivEtude')
    Stages=Stage.objects.filter(NivEtude=NivEtude_id)
    return render(request,'chained_dropdowns/StageNiv_dropdown_list_options.html',{'Stages':Stages})

    

def Statistiques (request):
    return get_Chart(request,2022,{})



def get_Chart (request,year): 
    years=Fiche_Stage.objects.all().values('AnneeCourante')
    labelss=[]
    ychart=[]
    fiches=Fiche_Stage.objects.filter(AnneeCourante=year,NivEtude=5)
    fiches_groupees=fiches.values('Organisme').annotate(countorg=Count('Organisme')).order_by()
    nbStagiaire=[]
    organismes2=[]
    ficheannee=Fiche_Stage.objects.filter(AnneeCourante=year)
    Organismes=ficheannee.values('Organisme').annotate(countorg=Count('Organisme')).order_by()
    Organismesprt=Organismes.filter(Organisme__typeOr='partenaire')
    annees=[]
    nbOrganismes=[]
    yearss=Fiche_Stage.objects.filter(NivEtude=5)
    years=yearss.values('AnneeCourante').annotate(countannee=Count('AnneeCourante')).order_by()
    types=Fiche_Stage.objects.filter(AnneeCourante=year).values('Stage__NivEtude').annotate(countStage=Count('Stage')).order_by()
    nbrtypes=[]
    typestage=[]
    for fg in fiches_groupees:
        organom=fg['Organisme']
        labelss.append(organom)
        ychart.append(fg['countorg'])
    

    for org in Organismesprt:
     nb=0
     ficheorg=ficheannee.filter(Organisme=org['Organisme'])
     
     for fic in ficheorg:
         i=fic.Etudiant.all()
         nb=nb + i.count()
     nbStagiaire.append(nb)
     organismes2.append(org['Organisme'])


    for annee in years:
        annees.append(annee['AnneeCourante'])
        nbOrganismes.append(nbOrgAnnee(annee['AnneeCourante']))

    for t in types:
        nbrtypes.append(t['countStage'])
        if t['Stage__NivEtude'] == 1 :
            typestage.append('CP1')

        if t['Stage__NivEtude'] == 3 :
            typestage.append('CS1')

        if t['Stage__NivEtude'] == 5 :
            typestage.append('PFE')

        

    dataJSON1 = dumps(labelss)
    dataJSON2 =dumps(ychart)
    dataJSON3 = dumps(nbStagiaire)
    dataJSON4 = dumps(organismes2)
    dataJSON5 = dumps(annees)
    dataJSON6 =dumps(nbOrganismes)
    dataJSON7 =dumps(nbrtypes)
    dataJSON8 =dumps(typestage)

    return render(request,'Statistiques.html',{'labelss':dataJSON1,'ychart':dataJSON2,'nbStagiaire':dataJSON3,'organismes2':dataJSON4,'annees':dataJSON5,'nbOrganismes':dataJSON6,'nbrtypes':dataJSON7,'typestage':dataJSON8,'years': years,'annees':annees})


def nbOrgAnnee (year):
    fiches=Fiche_Stage.objects.filter(AnneeCourante=year,NivEtude=5)
    fiches_groupees=fiches.values('Organisme').annotate(countorg=Count('Organisme')).order_by()
    nborg=fiches_groupees.count()

    return nborg







