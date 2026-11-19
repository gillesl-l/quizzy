"""Module qui gère le quiz."""
__author__ = "gilles_l"

from utils import lire_json


class Question:
    """Représente une question du quiz."""

    def __init__(self, donnees: dict):
        """Initialise une question."""
        self.id = donnees["id"]
        self.theme = donnees["theme"]
        self.question = donnees["question"]
        self.options = donnees["options"]
        self.reponse = donnees["reponse"]


class Quiz:
    """Représente un quiz."""

    def __init__(self, fichier: str):
        """Charge les questions depuis un fichier JSON."""
        donnees = lire_json(fichier)

        if not isinstance(donnees, list) or len(donnees) == 0:
            raise ValueError(
                "Le fichier ne contient aucune question valide."
            )

        self.questions = []

        for donnee in donnees:
            if not isinstance(donnee, dict):
                raise ValueError("Une question est mal formatée.")

            question = Question(donnee)

            if not isinstance(question.options, list):
                raise ValueError("Les options doivent être une liste.")

            if len(question.options) == 0:
                raise ValueError("Une question doit avoir des options.")

            if question.reponse not in question.options:
                raise ValueError(
                    "La réponse correcte doit être dans les options."
                )

            self.questions.append(question)

    def lancer(self) -> int:
        """Pose les questions et retourne le nombre de bonnes réponses."""
        score = 0

        for question in self.questions:
            print()
            print("Thème :", question.theme)
            print("Question", question.id, ":", question.question)

            lettres = []

            for i, option in enumerate(question.options):
                lettre = chr(97 + i)
                lettres.append(lettre)
                print(lettre, "-", option)

            while True:
                reponse = input(
                    "Votre réponse (a, b, c...) : "
                ).strip().lower()

                if reponse in lettres:
                    break

                print("Réponse invalide. Veuillez réessayer.")

            index = ord(reponse) - ord("a")
            choix = question.options[index]

            if choix == question.reponse:
                print("Bonne réponse !")
                score += 1
            else:
                print("Mauvaise réponse.")
                print("Réponse attendue :", question.reponse)

        total = len(self.questions)
        incorrectes = total - score

        print()
        print(" Résultat du quiz ")
        print("Score obtenu :", score, "/", total)
        print("Réponses correctes :", score)
        print("Réponses incorrectes :", incorrectes)

        return score
