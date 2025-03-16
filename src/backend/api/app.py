from flask import Flask, request, jsonify
from bson.objectid import ObjectId
from datetime import datetime
from utils.utils import is_valid_nir
from database import get_db

app = Flask(__name__)

# Connexion à la base de données
db = get_db()

# Endpoint pour lister les praticiens
@app.route('/praticiens', methods=['GET'])
def list_praticiens():
    praticiens = db.praticiens
    try:
        all_praticiens = list(praticiens.find())
        for praticien in all_praticiens:
            praticien['_id'] = str(praticien['_id'])
        return jsonify(all_praticiens), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint pour ajouter un patient
@app.route('/patients', methods=['POST'])
def add_patient():
    patients = db.patients
    data = request.get_json()

    if 'nom' not in data or 'prenom' not in data:
        return jsonify({'error': 'Nom et prénom sont obligatoires'}), 400

    patient = {
        'nom': data['nom'],
        'prenom': data['prenom'],
    }

    if 'nir' in data:
        if is_valid_nir(data['nir']):
            patient['nir'] = data['nir']
        else:
            return jsonify({'error': "Le NIR n'est pas valide"}), 400

    if 'date_naissance' in data:
        try:
            patient['date_naissance'] = datetime.strptime(
                data['date_naissance'], "%Y-%m-%d")
        except ValueError as ve:
            return jsonify({'error': str(ve)}), 400

    try:
        result = patients.insert_one(patient)
        return jsonify({'message': 'Patient ajouté', 'patient_id': str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint pour supprimer un patient par ID
@app.route('/patients/<patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    patients = db.patients
    try:
        result = patients.delete_one({'_id': ObjectId(patient_id)})
        if result.deleted_count == 0:
            return jsonify({'error': 'Patient non trouvé'}), 404
        return jsonify({'message': 'Patient supprimé'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint pour lister les patients
@app.route('/patients', methods=['GET'])
def list_patients():
    patients = db.patients
    try:
        all_patients = list(patients.find().sort([('nom', 1), ('prenom', 1)]))
        for patient in all_patients:
            patient['_id'] = str(patient['_id'])
        return jsonify(all_patients), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint pour ajouter un dispositif
@app.route('/dispositifs', methods=['POST'])
def add_dispositif():
    dispositifs = db.dispositifs
    data = request.get_json()

    if 'nom' not in data:
        return jsonify({'error': 'Nom est obligatoire'}), 400

    try:
        dispositif = {
            'nom': data['nom'],
            'description': data.get('description', '')
        }
        result = dispositifs.insert_one(dispositif)
        return jsonify({'message': 'Dispositif ajouté', 'dispositif_id': str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint pour lister les dispositifs
@app.route('/dispositifs', methods=['GET'])
def list_dispositifs():
    dispositifs = db.dispositifs
    try:
        all_dispositifs = list(dispositifs.find())
        for dispositif in all_dispositifs:
            dispositif['_id'] = str(dispositif['_id'])
        return jsonify(all_dispositifs), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint pour prescrire un dispositif à un patient
@app.route('/prescriptions', methods=['POST'])
def add_prescription():
    prescriptions = db.prescriptions
    data = request.get_json()

    if 'praticien_id' not in data or 'patient_id' not in data or 'dispositifs' not in data:
        return jsonify({'error': 'praticien_id, patient_id et dispositifs sont obligatoires'}), 400

    try:
        prescription = {
            'praticien_id': ObjectId(data['praticien_id']),
            'patient_id': ObjectId(data['patient_id']),
            'dispositifs': [
                {
                    'dispositif_id': ObjectId(dispositif['dispositif_id']),
                    'quantity': int(dispositif['quantity'])
                } for dispositif in data['dispositifs']
            ],
            'date_prescription': datetime.strptime(
                data['date_prescription'], "%Y-%m-%d") if 'date_prescription' in data else datetime.now(),
            'description': data['description'] if 'description' in data else '',
        }
        result = prescriptions.insert_one(prescription)
        return jsonify({'message': 'Prescription ajoutée', 'prescription_id': str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint pour obtenir toutes les prescriptions d'un patient par ID
@app.route('/prescriptions/patient/<patient_id>', methods=['GET'])
def get_prescriptions_by_patient(patient_id):
    prescriptions = db.prescriptions
    try:
        patient_prescriptions = list(prescriptions.find(
            {'patient_id': ObjectId(patient_id)}))
        for prescription in patient_prescriptions:
            prescription['_id'] = str(prescription['_id'])
            prescription['patient_id'] = str(prescription['patient_id'])
            prescription['dispositif_id'] = str(prescription['dispositif_id'])
        return jsonify(patient_prescriptions), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
