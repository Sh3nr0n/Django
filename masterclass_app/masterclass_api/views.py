from django.shortcuts import render
from django.contrib import messages
from django.db import connection
from .models import (Apprenants, Formateurs, Hobbies)
from .forms import (FormulaireHobbies)

# Create your views here.
# def accueil(request): #request est un argument obligatoire (toujours le premier argument et toujours appelé "request")
def accueil(request):
    if request.method == 'POST':
    	formulaire = FormulaireHobbies(request.POST)

    	if formulaire.is_valid():
    		try: 
    			formulaire.save()
    			messages.add_message(
    				request,
    				messages.SUCCESS,
    				"Vous avez réussi"
    			)
    		except: 
    			messages.add_message(
    				request,
    				messages.ERROR,
    				"Vous avez échoué"
    			)
    else: 
    	formulaire = FormulaireHobbies()
    hobbies = Hobbies.objects.all()
    return render(request, 'accueil.html', {
    	'formulaire':formulaire, 
    	'hobbies':hobbies
    }) 


    # return render(request, 'accueil.html') # Retourner quel fichier html afficher lorsqu'on retourne la vue
