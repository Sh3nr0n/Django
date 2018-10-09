from django import forms 

from .models import (Apprenants, Formateurs, Hobbies) # Import des modèles sous forme de tuple

class FormulaireHobbies (forms.ModelForm):

	class Meta: 
		model = Hobbies
		fields = ('type_hobbies', 'description')

	def __init__ (self, *args, **kwarg): # Importer des arguments dont le nombre n'est pas connu d'avance sous form de de tuples (*args) et de dictionnaires (**kwargs)
		super().__init__(*args, **kwarg)

	def save(self):
		type_hobbies = self.cleaned_data['type_hobbies']  # Verfication des données (cleaned_data) pour les inputs avec le nom "type_hobbies"
		description = self.cleaned_data['description']
		activite = Hobbies.objects.create( # Créé l'objet Hobbies et pour chacune de ses propriétés (ex : type_hobbies) on lui attribue une valeur égale à la variable définie au dessus ( type_hobbies)
			type_hobbies = type_hobbies,
			description = description
        )
