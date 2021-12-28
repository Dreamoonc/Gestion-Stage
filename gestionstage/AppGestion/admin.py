from django.contrib import admin
from .models import Stagiaire
from .models import Encadrant
from .models import OrganismedAccueil
from .models import Promoteur
from .models import TypeStage
from .models import Stage
from .models import Faire_Stage



admin.site.register(Stagiaire)
admin.site.register(Encadrant)
admin.site.register(OrganismedAccueil)
admin.site.register(Promoteur)
admin.site.register(TypeStage)
admin.site.register(Stage)
admin.site.register(Faire_Stage)