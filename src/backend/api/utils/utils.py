import re

# Vérification du NIR


def is_valid_nir(nir):
    """
    Vérifie si un NIR (Numéro d'Inscription au Répertoire) est valide.

    Un NIR valide doit respecter le format suivant :
    - Commence par 1 ou 2
    - Suivi de 2 chiffres pour l'année de naissance
    - Suivi de 2 chiffres pour le mois de naissance (01 à 12)
    - Suivi de 2 chiffres pour le département de naissance
    - Suivi de 6 chiffres pour un numéro unique
    - Se termine par 2 chiffres de contrôle

    Args:
        nir (str): Le NIR à vérifier.

    Returns:
        bool: True si le NIR est valide, False sinon.
    """
    pattern = r'^[12]\d{2}(0[1-9]|1[0-2])\d{2}\d{6}\d{2}$'
    return re.match(pattern, nir) is not None
