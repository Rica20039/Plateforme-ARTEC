import os
import pandas as pd
import numpy as np
import joblib
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow.keras.metrics import MeanSquaredError
from .models import QoSMetric, SanctionRecompense

def traiter_dataset(dataset):
    """Lit le fichier, prédit le QoS et génère les alertes automatiquement"""
    try:
        # 1. Charger l'IA
        model_path = os.path.join(settings.BASE_DIR, 'ml_models', 'modele_qos.h5')
        scaler_path = os.path.join(settings.BASE_DIR, 'ml_models', 'scaler_qos.pkl')
        
        # On ajoute custom_objects pour éviter les erreurs de métriques avec les nouvelles versions de Keras
        model = load_model(model_path, custom_objects={'mse': MeanSquaredError()})
        scaler = joblib.load(scaler_path)

        # 2. Lire le fichier (CSV ou Excel)
        chemin_fichier = dataset.fichier.path
        if chemin_fichier.endswith('.csv'):
            df = pd.read_csv(chemin_fichier)
        else:
            df = pd.read_excel(chemin_fichier)

        # 3. Vérifier si les bonnes colonnes sont présentes
        colonnes_requises = ['csr', 'debit', 'latence', 'disponibilite']
        if not all(col in df.columns for col in colonnes_requises):
            return False, f"Erreur : Le fichier doit contenir les colonnes : {', '.join(colonnes_requises)}"

        # 4. Analyser chaque ligne du fichier
        for index, row in df.iterrows():
            X_nouveau = np.array([[row['csr'], row['debit'], row['latence'], row['disponibilite']]])
            X_scaled = scaler.transform(X_nouveau)
            
            # L'IA fait sa prédiction
            score = float(model.predict(X_scaled, verbose=0).ravel()[0])
            score = np.clip(score, 0, 100) # Limiter entre 0 et 100

            # Donner une interprétation
            if score <= 40: interpretation = "Mauvaise qualité"
            elif score <= 70: interpretation = "Qualité moyenne"
            elif score <= 90: interpretation = "Bonne qualité"
            else: interpretation = "Excellente qualité"

            # Enregistrer le résultat dans la base
            QoSMetric.objects.create(
                dataset=dataset, csr=row['csr'], debit=row['debit'],
                latence=row['latence'], disponibilite=row['disponibilite'],
                score_qos=score, interpretation=interpretation
            )

            # 5. SANCTION OU FÉLICITATION AUTOMATIQUE
            if score <= 30:
                SanctionRecompense.objects.create(
                    operateur=dataset.operateur, type_alerte='sanction',
                    score_qos=score, message=f"Sanction automatique : Score critique de {score:.2f}/100."
                )
            elif score >= 85:
                SanctionRecompense.objects.create(
                    operateur=dataset.operateur, type_alerte='felicitation',
                    score_qos=score, message=f"Félicitation automatique : Très bonne qualité ({score:.2f}/100)."
                )

        # Marquer le fichier comme traité
        dataset.traite = True
        dataset.save()
        return True, "Fichier analysé par l'IA avec succès !"

    except Exception as e:
        return False, f"Erreur lors de l'analyse : {str(e)}"