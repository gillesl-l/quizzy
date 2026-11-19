"""Point d'entrée du programme de quiz."""
__author__ = "gilles_l"

import json

from quiz import Quiz
from user import enregistrer_score, afficher_scores
from utils import afficher_titre, demander_nom, demander_choix


def jouer(nom: str) -> None:
    """Lance un quiz et sauvegarde le résultat."""
    try:
        quiz = Quiz("data/questions.json")

        themes = []

        for question in quiz.questions:
            if question.theme not in themes:
                themes.append(question.theme)

        afficher_titre("Choix du thème")

        for i, theme in enumerate(themes):
            print(str(i + 1) + ".", theme)

        choix_valides = []

        for i in range(len(themes)):
            choix_valides.append(str(i + 1))

        choix = demander_choix(
            "Choisissez un thème : ",
            choix_valides
        )

        theme = themes[int(choix) - 1]

        quiz.questions = [
            question
            for question in quiz.questions
            if question.theme == theme
        ]

        score = quiz.lancer()

        total = len(quiz.questions)
        pourcentage = round(score / total * 100)

        enregistrer_score(nom, theme, pourcentage)

        print()
        print("Votre score :", pourcentage, "%")
        print("Votre résultat a été sauvegardé.")

    except FileNotFoundError:
        print("Erreur : fichier introuvable.")

    except json.JSONDecodeError:
        print("Erreur : un fichier JSON est mal formaté.")

    except (KeyError, TypeError, ValueError) as erreur:
        print("Erreur dans les données :", erreur)

    except OSError as erreur:
        print("Erreur lors de l'accès à un fichier :", erreur)


def main() -> None:
    """Affiche le menu principal."""
    afficher_titre("Bienvenue dans le quiz")

    nom = demander_nom()

    while True:
        afficher_titre("Menu principal")

        print("1. Jouer au quiz")
        print("2. Voir les résultats")
        print("3. Quitter")

        choix = demander_choix(
            "Votre choix : ",
            ["1", "2", "3"]
        )

        if choix == "1":
            jouer(nom)

        elif choix == "2":
            try:
                afficher_scores()

            except json.JSONDecodeError:
                print(
                    "Erreur : le fichier utilisateurs.json "
                    "est mal formaté."
                )

            except (KeyError, TypeError, ValueError) as erreur:
                print("Erreur dans les données :", erreur)

            except OSError as erreur:
                print("Erreur lors de la lecture du fichier :", erreur)

        else:
            print("Merci d'avoir joué ! Au revoir.")
            break


if __name__ == "__main__":
    main()
