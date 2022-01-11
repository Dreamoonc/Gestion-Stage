from django.forms import ModelForm
from .models import *

class StagiaireForm (ModelForm):
    class Meta:
        model=Stagiaire
        fields="__all__"
class EncadrantForm (ModelForm):
    class Meta:
        model=Encadrant
        fields="__all__"
class OrganismeForm (ModelForm):
    class Meta:
        model=Organisme
        fields="__all__"
class PromoteurForm (ModelForm):
    class Meta:
        model=Promoteur
        fields="__all__"
class StageForm (ModelForm):
    class Meta:
        model=Stage
        fields="__all__"
