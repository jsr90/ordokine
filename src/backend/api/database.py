from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis un fichier .env
load_dotenv(dotenv_path='config/.env')

# Obtenir l'URI de MongoDB à partir des variables d'environnement
MONGO_URI = os.getenv("MONGO_URI")
client = None
db = None

def get_db():
    """
    Établit une connexion avec la base de données MongoDB et assigne
    le client et la base de données aux variables globales `client` et `db`.

    Si la connexion est réussie, imprime un message de succès.
    En cas d'erreur, imprime le message d'erreur.
    """
    global client, db
    try:
        # Créer un client MongoDB
        client = MongoClient(MONGO_URI)
        # Sélectionner la base de données
        db = client.ordokine
        # Vérifier la connexion avec une commande ping
        db.command("ping")
        print("Connexion réussie à MongoDB")
        return db
    except Exception as e:
        print(f"Erreur de connexion: {str(e)}")
        return None
