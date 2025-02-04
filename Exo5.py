#Définition de la fonction compose
def compose(f, g):
    return lambda x: f(g(x))

#Composition de deux expressions lambda et test avec différentes entrées
double = lambda x: x * 2
ajoute_trois = lambda x: x + 3

# Composition des deux fonctions : (double(ajoute_trois(x)))
fonction_composee = compose(double, ajoute_trois)

# Tests
print("Résultats de la fonction composée :")
print(fonction_composee(5))   # (5 + 3) * 2 = 16
print(fonction_composee(10))  # (10 + 3) * 2 = 26
print(fonction_composee(0))   # (0 + 3) * 2 = 6