# Définition de la fonction calculateDiscount
def calculateDiscount(products, discount_percentage):
    total = 0
    for product in products:
        # Calculer le prix après réduction
        discounted_price = product['price'] * (1 - discount_percentage / 100)
        total += discounted_price
    return total

#liste de produits
products = [
    {"name": "Produit 1", "price": 500},
    {"name": "Produit 2", "price": 200},
    {"name": "Produit 3", "price": 150}
]

#Réduction de 20%
discount_percentage = 20

# Calculer le montant total après réduction
total_after_discount = calculateDiscount(products, discount_percentage)

# Afficher le résultat
print(f"Montant total après réduction de {discount_percentage}%: {total_after_discount}€")