from django.contrib import admin # Fichier qui ccontrole l'interface admin
from masterclass_api.models import * # Importe tous les modèles depuis l'application 'masterclas_app'
# Register your models here.

admin.site.register(Apprenants) #  Utilise le modèle "Apprenant" pour crééer un formulaire dans l'interface admin du site
admin.site.register(Formateurs)
admin.site.register(Hobbies)