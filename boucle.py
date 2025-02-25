thislist = ['apple', 'banana', 'cherry', 'Strawberry']
thislist = [li.lower() for li in thislist]
[print(f"{i+1}- {x}") for i, x in enumerate(thislist)]

txt = "***"
print(txt.center(13, '•'))

i = 1
for new in thislist:
	if "rr" in new:
		print(f"{i}- {new}")
		i += 1

lists = [
    {
        "fruits": ["banana", "apple"],
        "personne": ['Rakoto', "Rabe"],
        "auto" : ['bmw', 'citroen', 'peugeot']
    }
]

guess = input('Entrez un mot: ').lower()

if guess in lists[0]['fruits']:
    print("c'est un fruit")
elif guess in [person.lower() for person in lists[0]['personne']]:
    print("c'est une personne")
elif guess in [auto.lower() for auto in lists[0]['auto']]:
    print("c'est une voiture")
else:
    print("autres")