from storage import charger, sauvegarder
from models import Entree
from datetime import date
from tmdb import rechercher_film, resumer_resultats

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
        titre_recherche = input("Titre à rechercher : ")
        brut = rechercher_film(titre_recherche)
        resume = resumer_resultats(brut)

        for i, film in enumerate(resume, start=1):
            print(f"{i}. {film['titre']} ({film['annee']}) - {film['synopsis']}...")

        choix_film = int(input("Quel film (numéro) : "))
        film_choisi = brut["results"][choix_film - 1]

        statut = input("Statut : ")

        affiche_url = "https://image.tmdb.org/t/p/w500" + film_choisi["poster_path"]

        nouvelle_entree = Entree(
            titre=film_choisi["title"],
            annee=int(film_choisi["release_date"][0:4]),
            date_ajout=date.today(),
            statut=statut,
            affiche_url=affiche_url,
            synopsis=film_choisi["overview"],
        )
        entrees.append(nouvelle_entree)
        sauvegarder(entrees, chemin)

    elif choix =="2":
        for item in entrees:
                print(item.titre, item.annee, item.statut, item.affiche_url, item.date_ajout)
                
