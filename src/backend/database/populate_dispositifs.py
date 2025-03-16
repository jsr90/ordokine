from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis un fichier .env
load_dotenv(dotenv_path='config/.env')

# Obtenir l'URI de MongoDB à partir des variables d'environnement
MONGO_URI = os.getenv("MONGO_URI")

# Connexion à MongoDB
client = MongoClient(MONGO_URI)

# Sélectionner la base de données et la collection
db = client['ordokine']
dispositifs = db['dispositifs']

# Liste des dispositifs à insérer
dispositifs_data = [
    {'nom': 'Potences et soulève-malades',
        'description': 'Appareils destinés au soulèvement du malade'},
    {'nom': 'Matelas anti-escarres',
        'description': 'Matelas en mousse de haute résilience type gaufrier'},
    {'nom': 'Coussin anti-escarres',
        'description': 'Coussin en fibres siliconées ou en mousse monobloc'},
    {'nom': 'Barrières de lits et cerceaux',
        'description': 'Dispositifs de sécurité pour lits'},
    {'nom': 'Aide à la déambulation', 'description': 'Cannes, béquilles, déambulateur'},
    {'nom': 'Fauteuil roulant manuel',
        'description': 'Fauteuils roulants à propulsion manuelle de classe 1 (location < 3 mois)'},
    {'nom': 'Attelles souples orthopédiques',
        'description': 'Attelles souples de correction orthopédique de série'},
    {'nom': 'Ceintures lombaires de soutien',
        'description': 'Ceintures de soutien lombaire de série et bandes ceintures de série'},
    {'nom': 'Bandes de contention élastique',
        'description': 'Bandes et orthèses de contention souple élastique des membres de série'},
    {'nom': 'Sonde périnale', 'description': 'Sonde ou électrode cutanée périnale pour électrostimulation pour incontinence urinaire'},
    {'nom': 'Collecteurs d’urines',
        'description': 'Collecteurs d’urines, étuis péniens, pessaires, urinal'},
    {'nom': 'Attelles souples de posture',
        'description': 'Attelles souples de posture et/ou de repos de série'},
    {'nom': 'Embouts de cannes', 'description': 'Accessoires pour cannes'},
    {'nom': 'Talonnettes', 'description': 'Talonnettes avec évidement et amortissantes'},
    {'nom': 'Débitmètre de pointe', 'description': 'Aide à la fonction respiratoire'},
    {'nom': 'Pansements pour balnéothérapie',
        'description': 'Pansements secs ou étanches pour immersion'}
]

# Insérer les dispositifs si la collection est vide
if dispositifs.count_documents({}) == 0:
    result = dispositifs.insert_many(dispositifs_data)
    print(f"✅ {len(result.inserted_ids)} dispositifs insérés avec succès !")
else:
    print("⚠️ La collection 'dispositifs' contient déjà des données. Aucune insertion effectuée.")
