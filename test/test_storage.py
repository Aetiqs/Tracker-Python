import json
from models import Entree
from storage import sauvegarder
from storage import charger
from datetime import date

def test_sauvegarder(tmp_path):
    film1 = Entree(titre="Dune",
                   annee=2021,
                   date_ajout=date(2026, 8, 6),
                   statut="à voir",
                   affiche_url="www.exemple.com/dune.jpg",
                   note=4,
                   commentaire="tesssst")
    film2 = Entree(titre="Inception",
                   annee=2010,
                   date_ajout=date(2025, 3, 9),
                   statut="terminé",
                   affiche_url="www.exemple.com/inception.jpg",
                   note=9.0,
                   commentaire="Test")
    film3 = Entree(titre="Le Fabuleux Destin d'Amélie Poulain",
                   annee=2001,
                   date_ajout=date(2024, 11, 1),
                   statut="en cours",
                   affiche_url="www.exemple.com/amelie.jpg",
                    note= 8)
                    

    chemin = tmp_path / "backlog.json"
    sauvegarder([film1, film2, film3], chemin)

    with open(chemin) as f:
        data = json.load(f)

    assert len(data) == 3
    assert data[0]["titre"] == "Dune"
    assert data[1]["note"] == 9.0
    assert data[2]["statut"] == "en cours"


def test_charger (tmp_path):
    film1 = Entree(titre="Dune",
                       annee=2021,
                       date_ajout=date(2026, 8, 6),
                       statut="à voir",
                       affiche_url="www.exemple.com/dune.jpg",
                       note=4,
                       commentaire="tesssst")
    chemin = tmp_path / "backlog.json"
    sauvegarder([film1], chemin)

    resultat = charger(chemin)

    assert len(resultat) == 1
    assert resultat[0].titre == "Dune"
    assert resultat[0].date_ajout == date(2026, 8, 6)
    