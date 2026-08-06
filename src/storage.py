import json
from models import Entree
from dataclasses import asdict


#À droite du = : dico["date_ajout"] va chercher la valeur actuelle stockée dans le dictionnaire à la clé "date_ajout" (c'est un objet date, ex: le 6 août 2026). .isoformat() transforme cet objet date en texte ("2026-08-06").
#À gauche du = : dico["date_ajout"] = ... range ce nouveau texte à la même clé "date_ajout", en écrasant l'ancienne valeur (l'objet date).

def sauvegarder(entrees, chemin):
    data = []
    for item in entrees:
        dico = asdict(item)
        dico["date_ajout"] = dico["date_ajout"].isoformat()
        data.append(dico)

    with open(chemin, "w") as f:
        json.dump(data, f)
