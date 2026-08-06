from dataclasses import dataclass
from datetime import date

@dataclass  
class Entree:
    titre: str
    annee: int
    date_ajout: date
    statut: str
    affiche_url: str
    note: float = None
    commentaire: str = None
    synopsis: str = None




