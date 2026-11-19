"""Module qui gère les utilisateurs et leurs scores."""
__author__ = "gilles_l"

import json
from datetime import date


FICHIER_UTILISATEURS = "data/utilisateurs.json"


def charger_utilisateurs() -> dict:
    """Charge les utilisateurs depuis le fichier JSON."""
    try:
        with open(
            FICHIER_UTILISATEURS, "r", encoding="utf-8"
        ) as fichier:
            return json.load(fichier)

    except FileNotFoundError:
        return {}


def sauvegarder_utilisateurs(utilisateurs: dict) -> None:
    """Enregistre les utilisateurs dans le fichier JSON."""
    with open(
        FICHIER_UTILISATEURS, "w", encoding="utf-8"
    ) as fichier:
        json.dump(
            utilisateurs, fichier, ensure_ascii=False, indent=4
        )


def enregistrer_score(nom: str, theme: str, score: int) -> None:
    """Enregistre le score d'un utilisateur."""
    utilisateurs = charger_utilisateurs()

    nom_enregistre = nom

    for utilisateur in utilisateurs:
        if utilisateur.lower() == nom.lower():
            nom_enregistre = utilisateur
            break

    if nom_enregistre not in utilisateurs:
        utilisateurs[nom_enregistre] = {"scores": []}

    resultat = {
        "theme": theme,
        "score": score,
        "date": date.today().isoformat()
    }

    utilisateurs[nom_enregistre]["scores"].append(resultat)

    sauvegarder_utilisateurs(utilisateurs)


def afficher_scores() -> None:
    """Affiche les résultats de tous les utilisateurs."""
    utilisateurs = charger_utilisateurs()

    if len(utilisateurs) == 0:
        print("Aucun résultat enregistré.")
        return

    for nom, informations in utilisateurs.items():
        print()
        print("Utilisateur :", nom)

        for resultat in informations["scores"]:
            print("Thème :", resultat["theme"])
            print("Score :", resultat["score"], "%")
            print("Date :", resultat["date"])
