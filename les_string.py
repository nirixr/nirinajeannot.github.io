personnes = [
    {
        'nom': 'Rakoto',
        'prenom': 'benirina',
        'age': 43
    },
    {
        'nom': 'Rasoa',
        'prenom': 'Lalaina',
        'age': 36
    },
    {
        'nom': 'Rajo',
        'prenom': 'Juanito',
        'age': 11
    },
    {
        'nom': 'Raju',
        'prenom': 'Juana',
        'age': 7
    }
]

for i, personne in enumerate(personnes):
    nom = personne['nom'].upper()
    prenom = personne['prenom'].title()
    age = personne['age']
    nom_complet = f"{i + 1}. {nom} {prenom} / {age} ans"
    print(nom_complet)

nbr = len(personnes)
sumage = sum(personne['age'] for personne in personnes)
average = round(sumage / nbr)
print(f"====> average age : {average}")

pers1 = personnes[1]['nom']
print(pers1[::-1])
