# OrdoKiné <img src="assets/icon.png" alt="OrdoKiné" width="30"/> 

Ordokine est un projet conçu pour gérer la prescription de **dispositifs de kinésithérapie**. Ce projet vise à faciliter la création, la gestion et le suivi des prescriptions médicales, ainsi que l'administration des informations des patients et des professionnels prescripteurs.

Le projet est basé sur plusieurs technologies clés pour assurer une gestion efficace des prescriptions de kinésithérapie. **MongoDB** est utilisé comme base de données pour stocker les informations des patients, des praticiens et des dispositifs. Une **API** développée avec **Flask** génère les routes nécessaires pour interagir avec la base de données, permettant ainsi des opérations **CRUD** (Créer, Lire, Mettre à jour, Supprimer) sur les différentes collections. L'interface utilisateur est réalisée avec **Gradio**, offrant une expérience utilisateur intuitive pour la gestion des prescriptions et des patients. Enfin, **FPDF2** est utilisé pour générer des fichiers PDF des prescriptions, facilitant ainsi la distribution et l'impression des ordonnances.

## Arborescence du Projet

```
ordokine/
├── assets/
│   └── icon.png
├── config/
│   ├── .env
│   └── requirements.txt
├── data/
│   └── tests/
│       └── patients.json
├── README.md
├── LICENSE
├── src/
│   ├── backend/
│   │   ├── api/
│   │   │   ├── app.py
│   │   │   ├── database.py
│   │   └── database/
│   │       └── init_ordokine_db.py
│   ├── gradio/
│   │   ├── run.py
│   │   └── utils/
│   │       ├── generate_pdf.py
│   │       └── utils.py
├── tests/
│   └── test_patient_operations.py
```

## Installation

Pour installer les dépendances du projet, suivez les étapes suivantes :

1. Ajoutez l'URI de **MongoDB** dans le fichier `.env` :
    ```sh
    MONGO_URI=votre_mongo_uri
    ```
2. Activez l'environnement virtuel :
    ```sh
    path_to_venv/Scripts/activate
    ```
3. Installez les dépendances requises :
    ```sh
    pip install -r config/requirements.txt
    ```

## Utilisation

Pour exécuter le projet, utilisez les commandes suivantes :

1. Lancez l'**API** :
    ```sh
    python src/backend/api/app.py
    ```
2. Lancez le serveur **Gradio** :
    ```sh
    gradio src/gradio/run.py
    ```

## Fonctionnalités

Avec ce projet, vous pouvez :
- Générer des prescriptions pour les patients avec les dispositifs sélectionnés.
- Obtenir le **PDF** de la prescription.
- Ajouter des patients et des dispositifs de kinésithérapie.

## Améliorations à venir

Les améliorations suivantes sont prévues pour les futures versions :
- Ajout de la fonctionnalité de mise à jour des informations des patients et des dispositifs.
- Ajout de la fonctionnalité de suivi des prescriptions générées.
- Ajout de la fonctionnalité d'ajouter des prescripteurs.
- Intégration avec d'autres systèmes de gestion de la santé.
- Amélioration de l'interface utilisateur pour une meilleure expérience.

## Contribution

Si vous souhaitez contribuer à ce projet, veuillez suivre les étapes suivantes :

1. Faites un fork du dépôt.
2. Créez une nouvelle branche (`git checkout -b feature/nouvelle-fonctionnalité`).
3. Apportez vos modifications et faites un commit (`git commit -am 'Ajouter nouvelle fonctionnalité'`).
4. Poussez la branche (`git push origin feature/nouvelle-fonctionnalité`).
5. Créez une nouvelle Pull Request.

## Licence

Ce projet est sous licence **MIT**. Consultez le fichier LICENSE pour plus de détails.
