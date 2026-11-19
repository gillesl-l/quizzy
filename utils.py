"""Module qui contient les fonctions utilitaires."""
__author__ = "gilles_l"

import json


def afficher_titre(titre: str) -> None:
    """Affiche un titre."""
    print()
    print("=" * len(titre))
    print(titre)
    print("=" * len(titre))
    print()


def demander_nom() -> str:
    """Demande le nom de l'utilisateur."""
    while True:
        nom = input("Entrez votre nom : ").strip()

        if nom != "":
            return nom

        print("Erreur : le nom ne peut pas être vide.")


def demander_choix(message: str, choix_valides: list) -> str:
    """Demande un choix valide à l'utilisateur."""
    while True:
        choix = input(message).strip()

        if choix in choix_valides:
            return choix

        print("Choix invalide. Veuillez réessayer.")


def lire_json(chemin: str):
    """Lit et retourne les données d'un fichier JSON."""
    with open(chemin, "r", encoding="utf-8") as fichier:
        return json.load(fichier)


def ecrire_json(chemin: str, donnees) -> None:
    """Enregistre des données dans un fichier JSON."""
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(
            donnees,
            fichier,
            ensure_ascii=False,
            indent=4
        )
