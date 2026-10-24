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