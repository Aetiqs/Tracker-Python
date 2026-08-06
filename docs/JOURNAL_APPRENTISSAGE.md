# Journal d'apprentissage

Ce fichier recense les notions apprises au fil du développement du projet, pour garder une trace de ce qui a été compris et pourquoi. Un nouvel add à chaque fois qu'un concept nouveau (ou une bonne pratique) est introduit.

Format d'une entrée :

```
## <Notion>
**Date** : AAAA-MM-JJ
**C'est quoi** : explication courte
**Pourquoi ça compte** : l'intérêt concret / le problème que ça résout
```

---

## Backlog
**Date** : 2026-08-06
**C'est quoi** : terme issu de l'agile/product management — la liste de tout ce qui est "en attente de traitement". Dans ce projet, le backlog = la liste des films/séries à voir, en cours, ou terminés.
**Pourquoi ça compte** : vocabulaire courant en dev/agile (ex. "product backlog"), utile à connaître au-delà de ce projet.

## `@dataclass`
**Date** : 2026-08-06
**C'est quoi** : décorateur Python qui génère automatiquement le code répétitif d'une classe qui ne sert qu'à stocker des données (constructeur, affichage, comparaison...).
**Pourquoi ça compte** : évite du code répétitif par rapport à une classe classique, et donne de l'autocomplétion + de la vérification de types — la même approche que dans du code de production.

## `Enum`
**Date** : 2026-08-06
**C'est quoi** : type Python qui restreint une variable à un ensemble fixe de valeurs nommées (ex. les statuts possibles d'une entrée : à voir / en cours / terminé).
**Pourquoi ça compte** : évite les erreurs de saisie sur des chaînes de caractères libres (`"Terminé"` vs `"terminé"` vs `"fini"`), et l'éditeur peut proposer l'autocomplétion.

## `Enum` vs `str` : un choix, pas une obligation
**Date** : 2026-08-06
**C'est quoi** : `Enum` fait partie de la bibliothèque standard de Python (pas de `pip install` nécessaire), mais utiliser un simple `str` pour un champ à valeurs fixes (ex. `statut`) reste valide, surtout en phase d'apprentissage des fondamentaux.
**Pourquoi ça compte** : mieux vaut solidifier les bases (types simples, fonctions, dataclass) avant d'empiler les abstractions. Migrer un `str` vers un `Enum` plus tard est un bon exercice de refactoring — pas une urgence.

## Décorateurs (`@...`)
**Date** : 2026-08-06
**C'est quoi** : une ligne commençant par `@`, placée juste au-dessus d'une fonction ou d'une classe (collée, sans ligne vide entre les deux), qui "enrichit" automatiquement ce qui suit. Exemple : `@dataclass` au-dessus de `class Entree:` génère automatiquement le constructeur et d'autres méthodes.
**Pourquoi ça compte** : syntaxe très courante en Python (Flask/FastAPI, tests avec pytest, etc.) — se reconnaît à vue mais ne se "devine" pas, il faut l'avoir vue une fois.

## Blocs de code : `:` et indentation
**Date** : 2026-08-06
**C'est quoi** : toute ligne qui ouvre un bloc (`class ... :`, `def ... :`, `if ... :`, `for ... :`) se termine par deux-points `:`. Tout ce qui appartient à ce bloc doit être indenté d'un cran (généralement 4 espaces) en dessous. Le décorateur et la ligne `class`/`def` qu'il décore doivent, eux, être au même niveau d'indentation (aucun décalage entre les deux).
**Pourquoi ça compte** : erreur très fréquente en débutant — un `:` oublié ou une indentation incohérente provoque une `SyntaxError` ou un `IndentationError`. Contrairement à d'autres langages (accolades `{}`), en Python l'indentation fait partie de la syntaxe, pas juste du style.

## Type optionnel : `float | None` vs `Optional[float]`
**Date** : 2026-08-06
**C'est quoi** : deux syntaxes strictement équivalentes pour dire "soit ce type, soit rien (`None`)". `float | None` est la syntaxe moderne (Python 3.10+), `Optional[float]` (du module `typing`) est l'ancienne syntaxe, encore très répandue dans du code existant.
**Pourquoi ça compte** : utile pour un champ pas toujours rempli (ex. `note` avant que le film soit noté). Les deux se croisent souvent en lisant du code d'autres projets, donc bon de connaître les deux même si on n'en utilise qu'une.

## Raccourci clavier Mac (AZERTY) : `|`
**Date** : 2026-08-06
**C'est quoi** : `Option (⌥) + Maj (⇧) + L`
**Pourquoi ça compte** : caractère utilisé pour les types "soit... soit..." (`float | None`), pas évident à trouver sur un clavier français.

## Type autorisé vs valeur par défaut
**Date** : 2026-08-06
**C'est quoi** : deux notions indépendantes sur un champ de dataclass. Le **type** (`float | None`) dit quelles valeurs sont acceptées dans le champ (ici : un nombre, ou la valeur spéciale `None` qui représente "aucune valeur"). Le **défaut** (`= None`) dit ce que Python utilise automatiquement si le champ n'est pas précisé à la création de l'objet. Sans défaut, même un champ de type optionnel doit être fourni explicitement à chaque création.
**Pourquoi ça compte** : erreur de compréhension fréquente en dataclass — croire qu'un type optionnel suffit à rendre le champ "non obligatoire" à la création, alors que c'est le `=` qui rend le champ optionnel dans le constructeur.

## Ordre des champs dans un `@dataclass`
**Date** : 2026-08-06
**C'est quoi** : tous les champs **sans** valeur par défaut doivent être déclarés **avant** ceux qui en ont une. Sinon, Python lève une erreur (`TypeError: non-default argument follows default argument`).
**Pourquoi ça compte** : ça a une conséquence concrète sur l'organisation du modèle — un champ obligatoire (ex. `affiche_url`) ne peut pas être placé après des champs optionnels (`note`, `commentaire`), même si ça semblerait plus logique de le mettre à la fin.

## `pytest` : conventions de nommage
**Date** : 2026-08-06
**C'est quoi** : `pytest` découvre les tests automatiquement selon des règles de nommage strictes — le fichier doit s'appeler `test_xxx.py` (ou `xxx_test.py`), et chaque fonction de test doit commencer par `test_`. Sans ça, `pytest` ignore silencieusement le fichier/la fonction (pas d'erreur, juste "0 test trouvé").
**Pourquoi ça compte** : `pytest` n'a pas besoin qu'on lui liste les tests un par un — il les trouve tout seul dans le projet grâce à cette convention, mais seulement si elle est respectée à la lettre.

## `pytest.ini` et `pythonpath`
**Date** : 2026-08-06
**C'est quoi** : fichier de config à la racine du projet qui indique à `pytest` où chercher les modules à importer (ex: `pythonpath = src` pour que `from storage import ...` fonctionne depuis un test situé dans `test/`, alors que le code est dans `src/`).
**Pourquoi ça compte** : sans ça, lancer `pytest` depuis la racine provoque une erreur `ModuleNotFoundError`, car Python ne cherche pas automatiquement dans `src/`.

## Fixtures pytest (ex: `tmp_path`)
**Date** : 2026-08-06
**C'est quoi** : un outil fourni automatiquement par `pytest` quand on le demande en paramètre d'une fonction de test, en l'appelant par son nom exact (ex: `def test_x(tmp_path):`). `tmp_path` fournit un dossier temporaire unique, supprimé automatiquement après le test.
**Pourquoi ça compte** : permet de tester du code qui écrit des fichiers sans polluer le vrai projet avec des fichiers de test qui traînent.

## `with` (context manager)
**Date** : 2026-08-06
**C'est quoi** : bloc qui garantit qu'une ressource (ex: un fichier ouvert avec `open()`) est correctement "nettoyée" (fermée) à la fin du bloc, même si une erreur survient en cours de route. Syntaxe : `with open(chemin) as f: ...` — `f` n'est utilisable qu'à l'intérieur du bloc indenté.
**Pourquoi ça compte** : sans `with`, il faut fermer le fichier manuellement (`f.close()`), et un oubli — ou une erreur qui interrompt le code avant le `close()` — peut laisser le fichier ouvert/verrouillé. `open()` est un exemple de "context manager" ; on en recroisera d'autres (ex: connexions DB en V3).

## `assert`
**Date** : 2026-08-06
**C'est quoi** : instruction qui vérifie qu'une condition est vraie. Si vraie, rien ne se passe. Si fausse, Python lève une `AssertionError` et arrête l'exécution à cet endroit, avec le détail de ce qui était attendu vs trouvé.
**Pourquoi ça compte** : brique de base de tout test — on écrit une fois "je m'attends à ce que X soit vrai", et on peut relancer cette vérification à volonté après chaque modification du code, sans avoir à vérifier à l'œil à chaque fois.

## Workflow pour ajouter une dépendance externe
**Date** : 2026-08-06
**C'est quoi** : à chaque fois qu'on ajoute un package externe (ex: `pytest`, `python-dotenv`) au projet, toujours la même séquence :
1. `pip install nom_du_package` (installe dans le `.venv` activé)
2. `pip freeze | grep nom_du_package` (récupère la version exacte installée)
3. Ajouter la ligne `nom_du_package==version` dans `requirements.txt` (fige la version pour la reproductibilité)
**Pourquoi ça compte** : `requirements.txt` doit toujours refléter fidèlement ce qui est réellement installé et utilisé par le projet — sinon quelqu'un (ou soi-même sur une autre machine) qui fait `pip install -r requirements.txt` ne retombe pas sur le même environnement, et peut avoir des bugs différents selon la version installée.

## Champs / schéma de données
**Date** : 2026-08-06
**C'est quoi** : les "champs" définis pour une entrée du backlog (titre, année, statut, note...) ne sont pas encore une vraie base de données en V1 (stockage JSON) — mais c'est le même schéma qui deviendra les colonnes de la table SQLite en V3.
**Pourquoi ça compte** : bien modéliser les données dès le départ évite de tout redéfinir plus tard.
