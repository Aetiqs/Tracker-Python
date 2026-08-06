from storage import charger, sauvegarder
from models import Entree
from datetime import date

chemin = "data/backlog.json"

try:
    entrees = charger(chemin)
except FileNotFoundError:
    entrees=[]



while True:
    print("1. Ajouter un film")
    print("2. Lister les films")
    print("3. Quitter")
    choix = input("Ton choix : ")

    if choix == "3":
        break
    elif choix == "1":
        titre2 = input("Titre : ")
        annee2 = int(input("Année : "))
        statut2 = input("Statut : ")
        affiche_url2 = input("Affiche (URL) : ")
        date_ajout2 = date.today()
        nouvelle_entree = Entree(titre=titre2, annee=annee2, statut=statut2, affiche_url=affiche_url2, date_ajout=date_ajout2)
        entrees.append(nouvelle_entree)
        sauvegarder(entrees, chemin)

    elif choix =="2":
        for item in entrees:
            print(item.titre, item.annee, item.statut, item.affiche_url, item.date_ajout)
            
