#liste de mots
mots = ["voiture", "volant", "avion", "zebre", "zoo", "antilope", "table", "tonneau"]

#expression lambda pour filtrer les mots qui commencent par "a"
mots_avec_a = list(filter(lambda mot: mot.startswith("z"), mots))
print("Mots qui commencent par 'a' :", mots_avec_a)

#clôture pour compter les mots ayant plus de 5 caractères
def compteur_mots_longueur(liste_mots):
    def compter():
        return len([mot for mot in liste_mots if len(mot) > 5])
    return compter

compteur = compteur_mots_longueur(mots)
print("Nombre de mots avec plus de 5 caractères :", compteur())