# Plateforme ARTEC - Régulation Télécom & QoS

## 📝 Présentation
Cette plateforme permet à l'ARTEC de réguler la qualité de service des opérateurs (YAS, Orange, Airtel). 
Elle intègre un modèle d'Intelligence Artificielle (TensorFlow) pour l'analyse de fichiers CSV/Excel, un système de sanctions/félicitations automatiques, une messagerie interne, des sondages, et un espace public citoyen.

## 🚀 Comment lancer le projet (Instructions pour le professeur)

### 1. Prérequis
- Python installé sur votre machine.
- Avoir téléchargé le projet (Download ZIP) et l'avoir décompressé.

### 2. Installation
Ouvrez un terminal dans le dossier du projet et exécutez :

```bash
# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement (Windows)
.venv\Scripts\activate

# Installer les librairies (Important : installer manuellement pour éviter les conflits de versions)
pip install django tensorflow pandas openpyxl scikit-learn joblib
## 🔑 Comptes de test (Déjà configurés dans la base de données)

Pour faciliter la correction, la base de données est déjà fournie avec des comptes et des données de démonstration prêts à l'emploi. **Vous n'avez pas besoin de créer un compte administrateur ni de faire de migrations.**

Voici les identifiants pour tester la plateforme (allez sur `/login/`) :

*   **Compte ARTEC (Régulateur) :**
    *   Nom d'utilisateur : `admin` (remplace par ton vrai nom d'utilisateur)
    *   Mot de passe : `rica2003` (remplace par ton vrai mot de passe)

*   **Compte Opérateur (ex: Orange) :**
    *   Nom d'utilisateur : `orange_test` (remplace par ton vrai nom d'utilisateur opérateur)
    *   Mot de passe : `org12345678` (remplace par ton vrai mot de passe)