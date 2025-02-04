# Définition de la fonction create_multiplier
def create_multiplier(n):
    return lambda x: x * n

#Création des fonctions double et triple
double = create_multiplier(2)
triple = create_multiplier(3)

#Boucle pour tester les fonctions avec chaque valeur
test_values = [2, 4, 10]

for val in test_values:
    print(f"double({val}) = {double(val)}")
    print(f"triple({val}) = {triple(val)}")