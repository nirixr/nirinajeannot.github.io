prix_vente = {
    'sakay': {
        'pm': 400,
        'mm': 700,
        'gm': 1500
    }
}

produits = {
    'sakay': {
        'pm': prix_vente['sakay']['pm'] * 0.6, 
        'mm': prix_vente['sakay']['mm'] * 0.6,
        'gm': prix_vente['sakay']['gm'] * 0.6
    },
}

benefice1 = prix_vente['sakay']['pm'] * (1 - 0.6)
benefice2 = prix_vente['sakay']['mm'] * (1 - 0.6)
benefice3 = prix_vente['sakay']['gm'] * (1 - 0.6)
print(benefice1, benefice2, benefice3)

capacite_rev1_hebdo = {
    'pm': 14,
    'mm': 1,
    'gm': 1
}

frequence = 4
charges = {
    "directeur": {
        "banque": 640000,
        "locaux": 150000,
        "ecolage": 55000,
        "sakafo": 130000,
        "epargne": 250000,
        "carburant": 80000,
        "autre": 100000
    },
    "employee" : {
        "salaire1": 150000,
        "salaire2": 150000,
        "sakafo": 2000 * 2 * 30,
    },
    "frais": {
        "jirama": 50000,
        "livraison": 40000 * frequence
    }
}

jour = 6

# Calculer la somme totale des charges mensuelles
def somme_charges(charges):
    total = 0
    for key, value in charges.items():
        if isinstance(value, dict):
            total += sum(value.values())
        else:
            total += value
    return total

ca_mensuelle = somme_charges(charges)

def objectif_hebdo(ca_mensuelle, prix, hebdo):
    return round(ca_mensuelle / prix / hebdo)

def nombre_revendeur(capacite_rev1_hebdo, objectif_hebdo):
    return round(objectif_hebdo / capacite_rev1_hebdo)

# Calculer la proportion des ventes pour chaque format
total_capacite = sum(capacite_rev1_hebdo.values())
proportions = {format: capacite / total_capacite for format, capacite in capacite_rev1_hebdo.items()}

# Répartir les charges proportionnellement
charges_proportionnelles = {format: ca_mensuelle * proportion for format, proportion in proportions.items()}

for produit, formats in produits.items():
    for format, prix in formats.items():
        obj_hebdo = objectif_hebdo(charges_proportionnelles[format], prix, frequence)
        nb_revendeurs = nombre_revendeur(capacite_rev1_hebdo[format], obj_hebdo)
        print(f"Produit: {produit} ({format})")
        print(f"Objectif journalier : {round(obj_hebdo / jour)}")
        print(f"Objectif hebdomadaire : {obj_hebdo}")
        print(f"Nombre de revendeurs : {nb_revendeurs}")
        print("*********-----------************")

ca_mensuelle = f"{ca_mensuelle:,}".replace(',', ' ')  
print(f"Chiffre d'affaire : {ca_mensuelle} Ar")
