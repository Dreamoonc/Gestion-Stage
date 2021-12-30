from django.contrib import admin
from .models import Stagiaire
from .models import Encadrant
from .models import Organisme
from .models import Promoteur
from .models import Stage
from .models import Fiche_Stage



admin.site.register(Stagiaire)
admin.site.register(Encadrant)
admin.site.register(Organisme)
admin.site.register(Promoteur)
admin.site.register(Stage)
admin.site.register(Fiche_Stage)