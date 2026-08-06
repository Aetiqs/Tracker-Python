import os
from dotenv import load_dotenv
import requests

load_dotenv ()
cle_api = os.getenv("TMDB_API_KEY")


def rechercher_film(titre):
    reponse = requests.get(
        "https://api.themoviedb.org/3/search/movie",
        params={"api_key": cle_api, "query": titre}
    )
    return reponse.json()

def resumer_resultats(resultats_bruts):
    resume = []
    for film in resultats_bruts["results"][:5]:
        resume.append({
            "titre": film["title"],
            "annee": film["release_date"][0:4],
            "synopsis": film["overview"][0:100],
        })
    return resume