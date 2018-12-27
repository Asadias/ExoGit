
#-*-coding:Latin-1 -*
# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non

import os 	#on importe le module os complet
			#avec ses fonctions pour dialoguer avec le sys

annee = input("Saisissez une année : ")		# On attend que l'utilisateur fournisse l'année qu'il désire tester
annee = int(annee) 		# Risque d'erreur si l'utilisateur n'a pas saisi un nombre

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")
	
os.system ("pause")