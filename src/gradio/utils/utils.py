from datetime import datetime
import requests
from utils.generate_pdf import generate_pdf

# URL de l'API
URL_BASE = "http://127.0.0.1:5000"

def obtenir_praticiens():
    """
    Récupère la liste des praticiens depuis l'API.
    """
    response = requests.get(f"{URL_BASE}/praticiens")
    return response.json()

def obtenir_patients():
    """
    Récupère la liste des patients depuis l'API.
    """
    response = requests.get(f"{URL_BASE}/patients")
    return response.json()

def obtenir_dispositifs():
    """
    Récupère la liste des dispositifs depuis l'API.
    """
    response = requests.get(f"{URL_BASE}/dispositifs")
    return response.json()

def ajouter_patient(nom, prenom, date_naissance=None, nir=None):
    """
    Ajoute un nouveau patient dans la base de données via l'API.
    """
    if len(nom) < 3 or len(prenom) < 3:
        return "Erreur: le nom et le prenom doivent contenir au moins 3 caractères."

    patient = {
        "nom": nom.upper(),
        "prenom": prenom.capitalize()
    }
    if date_naissance is not None:
        patient["date_naissance"] = date_naissance
    if nir is not None and nir != "":
        patient["nir"] = nir

    try:
        response = requests.post(f"{URL_BASE}/patients", json=patient)
        response.raise_for_status()
        return "Patient ajouté avec succès."
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de l'ajout du patient: {e}"

def ajouter_dispositif(nom, description=None):
    """
    Ajoute un nouveau dispositif dans la base de données via l'API.
    """
    if len(nom) < 3:
        return "Erreur: le nom doit contenir au moins 3 caractères."

    dispositif = {
        "nom": nom.capitalize()
    }
    if description is not None:
        dispositif["description"] = description

    try:
        response = requests.post(f"{URL_BASE}/dispositifs", json=dispositif)
        response.raise_for_status()
        return "Dispositif ajouté avec succès."
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de l'ajout du dispositif: {e}"

def generer_ordonnance(praticien, patient, dispositifs, date):
    """
    Génère une ordonnance pour un patient avec les dispositifs prescrits.
    """
    dispositifs_ = [{"dispositif_id": d["_id"], "quantity": d.get("quantity", 1)} for d in dispositifs]
    prescription = {
        "praticien_id": praticien["_id"],
        "patient_id": patient["_id"],
        "dispositifs": dispositifs_,
        "date_prescription": date
    }
    try:
        response = requests.post(f"{URL_BASE}/prescriptions", json=prescription)
        response.raise_for_status()
        prescription['_id'] = response.json()["prescription_id"]
        return generate_pdf(praticien, patient, dispositifs, prescription)
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de la génération de l'ordonnance: {e}"