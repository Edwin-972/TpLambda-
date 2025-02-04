import time

#Définition de la fonction memoize
def memoize(f):
    cache = {}  # Dictionnaire pour stocker les résultats
    def memorized_function(x):
        if x in cache:
            return cache[x]  # Retourne la valeur déjà calculée
        result = f(x)  # Calcule la valeur si elle n'est pas en cache
        cache[x] = result  # Stocke le résultat dans le cache
        return result
    return memorized_function  # Retourne la fonction mémorisée


# Fonction de calcul de la factorielle
@memoize
def factorielle(n):
    return 1 if n == 0 else n * factorielle(n - 1)

# Fonction de calcul de Fibonacci
@memoize
def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

# Mesure du temps d'exécution pour des calculs répétés
n = 35

# Test sans mémoïsation pour comparaison
def test_fibonacci_sans_memo(n):
    if n <= 1:
        return n
    return test_fibonacci_sans_memo(n - 1) + test_fibonacci_sans_memo(n - 2)

print("Calcul de Fibonacci avec mémoïsation :")
start_time = time.time()
print(f"Fibonacci({n}) =", fibonacci(n))
print("Temps d'exécution :", time.time() - start_time, "secondes")

print("\nCalcul de Factorielle avec mémoïsation :")
start_time = time.time()
print(f"Factorielle({n}) =", factorielle(n))
print("Temps d'exécution :", time.time() - start_time, "secondes")

