#Définition de la fonction filterMap
def filterMap(filtre, transformation, liste):
    return [transformation(x) for x in liste if filtre(x)]

#Filtrer et transformer une liste de chaînes de caractères
mots = ["python", "", "lambda", "exercice", "", "code"]

# Filtrage : Supprimer les chaînes vides
# Transformation : Convertir en majuscules
resultat = filterMap(lambda x: x != "", lambda x: x.upper(), mots)

# Affichage du résultat
print("Résultat trouver après filterMap :", resultat)  # ['PYTHON', 'LAMBDA', 'EXERCICE', 'CODE']