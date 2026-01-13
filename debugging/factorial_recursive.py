#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Description:
		Calcule le factoriel d’un nombre entier de manière récursive.
		Le factoriel d’un nombre n est le produit de tous les entiers
		positifs inférieurs ou égaux à n.

	Paramètres:
		n (int): Un nombre entier positif ou nul dont on veut calculer
				 le factoriel.

	Retour:
		int: Le factoriel de n.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

# Récupère l’argument passé en ligne de commande,
# le convertit en entier et calcule son factoriel
f = factorial(int(sys.argv[1]))

# Affiche le résultat
print(f)
