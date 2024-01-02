import random

class Personne:
    def __init__(self, nom, sexe):
        self.nom = nom
        self.sexe = sexe

class Famille:
    def __init__(self, nom_famille):
        self.nom_famille = nom_famille
        self.enfants = []

    def ajouter_enfant(self, enfant):
        self.enfants.append(enfant)

def creation_famille(nom_famille, nombre_enfants):
    famille = Famille(nom_famille)
    for i in range(nombre_enfants):
        sexe_enfant = random.choice(["garçon", "fille"])
        enfant = Personne(f"{nom_famille}_Enfant{i+1}", sexe_enfant)
        famille.ajouter_enfant(enfant)
    return famille

def former_nouvelle_famille(famille1, famille2):
    nouvelle_famille = Famille(f"{famille1.nom_famille}_{famille2.nom_famille}_Merged")

    for enfant_famille1 in famille1.enfants:
        for enfant_famille2 in famille2.enfants:
            if enfant_famille1.sexe != enfant_famille2.sexe:
                # Créer un nouvel enfant en associant les enfants de familles différentes
                enfant_merged = Personne(f"{enfant_famille1.nom}_{enfant_famille2.nom}", random.choice(["garçon", "fille"]))
                nouvelle_famille.ajouter_enfant(enfant_merged)

    return nouvelle_famille

# Création des deux familles initiales
famille_a = creation_famille("FamilleA", 2)
famille_b = creation_famille("FamilleB", 2)

# Formation de la nouvelle famille en associant les enfants des deux familles initiales
nouvelle_famille = former_nouvelle_famille(famille_a, famille_b)

# Affichage des membres de la nouvelle famille avec une structure de générations
print(f"Membres de la nouvelle famille ({nouvelle_famille.nom_famille}):")
generation = 1
for enfant in nouvelle_famille.enfants:
    print(f"Génération {generation} - {enfant.nom} ({enfant.sexe})")
    generation += 1
