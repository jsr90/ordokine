import pytest
import requests
import json
import os

# URL de l'API
BASE_URL = "http://127.0.0.1:5000"

# Charger les données de patients_with_expected_status.json
with open("data/tests/patients.json", "r", encoding="utf-8") as file:
    patients_data = json.load(file)

# Liste pour stocker les IDs des patients valides
valid_patient_ids = []


@pytest.mark.parametrize("patient_data", patients_data)
def test_add_patient(patient_data):
    patient = patient_data["patient"]
    expected_status = patient_data["expected_status"]
    response = requests.post(f"{BASE_URL}/patients", json=patient)
    if response.status_code == 201:
        valid_patient_ids.append(response.json().get("patient_id"))
    assert response.status_code == expected_status, f"Échec pour le patient: {patient}"


def test_delete_patient():
    print(len(valid_patient_ids))
    for patient_id in valid_patient_ids:
        # Supprimer le patient ajouté
        response = requests.delete(f"{BASE_URL}/patients/{patient_id}")
        assert response.status_code == 200, f"Échec de la suppression du patient avec l'ID: {patient_id}"


if __name__ == "__main__":
    pytest.main()
    test_delete_patient()
