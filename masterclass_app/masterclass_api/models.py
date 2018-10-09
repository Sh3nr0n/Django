from django.db import models # permet à l'ORM d'aller chercher les infos dans le fichier settings

# Create your models here.
from django.db import models

class Hobbies(models.Model):
	type_hobbies = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.type_hobbies

class Formateurs(models.Model):
	nom = models.CharField(max_length=100)
	prenom = models.CharField(max_length=100)
	mail = models.EmailField(unique=True)
	hobbies = models.ForeignKey(Hobbies, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.nom} {self.prenom}'

class Apprenants(models.Model):
	nom = models.CharField(max_length=100)
	prenom = models.CharField(max_length=100)
	mail = models.EmailField(unique=True)
	hobbies = models.ForeignKey(Hobbies, on_delete=models.CASCADE)
	formateurs = models.ForeignKey(Formateurs, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.nom} {self.prenom}'