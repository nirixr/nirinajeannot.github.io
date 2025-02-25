def my_list(produits):
    for i, produit in enumerate(produits):
        produit = produit.capitalize()
        print(f"{i+1}- {produit}")

def my_list(produits):
    produits_capitalized = [produit.capitalize() for produit in produits]
    for i, produit in enumerate(produits_capitalized):
        print(f"{i+1}- {produit}")

