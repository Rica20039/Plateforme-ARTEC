# Plateforme ARTEC - Régulation Télécom & QoS

## 📝 Description
Cette plateforme permet à l'ARTEC de réguler la qualité de service (QoS) des opérateurs (YAS, Orange, Airtel). 
Elle intègre un modèle d'Intelligence Artificielle (TensorFlow) pour l'analyse des fichiers (CSV/Excel), un système de sanctions/félicitations automatiques, un chat, des sondages et un espace citoyen.

## 🛠️ Technologies utilisées
- **Backend** : Django (Python)
- **Base de données** : SQLite (développement)
- **Intelligence Artificielle** : TensorFlow / Keras, Scikit-learn, Pandas
- **Frontend** : HTML, CSS (Design personnalisé)

## 🚀 Comment lancer le projet en local
1. Cloner le projet : `git clone [LIEN_DE_TON_REPO]`
2. Créer un environnement virtuel : `python -m venv .venv`
3. Activer l'environnement : `.venv\Scripts\activate` (Windows)
4. Installer les dépendances : `pip install -r requirements.txt`
5. Lancer le serveur : `python manage.py runserver`

## 👥 Comptes de test
- ARTEC : `/login/` (Compte admin)
- Opérateur : `/login/` (Compte Orange/YAS/Airtel)
- Public : `/` (Accessible sans compte)