# Définition d'une expression lambda pour le carré d'un nombre
carre = lambda x: x ** 2

# liste de nombres
nombres = [1, 2, 3, 4, 5]
carres = list(map(carre, nombres))
print("Carrés:", carres)

#somme de deux nombres
somme = lambda a, b: a + b

#calcul somme totale
from functools import reduce
total = reduce(somme, nombres)
print("Somme totale:", total)