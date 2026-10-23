import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler
import joblib

# 1. Les données
X = np.array([
[82.5, 3.2, 85.0, 91.5], [85.1, 4.5, 72.0, 93.0], [88.8, 5.8, 65.0, 94.8],
[90.2, 6.7, 58.0, 95.5], [91.5, 7.9, 52.0, 96.2], [92.8, 8.8, 48.0, 97.0],
[93.6, 9.7, 44.0, 97.5], [94.5, 10.9, 40.0, 98.0], [95.1, 12.1, 36.0, 98.5],
[96.0, 13.5, 32.0, 99.0], [78.5, 2.5, 95.0, 89.0], [81.7, 3.8, 82.0, 91.5],
[87.2, 5.1, 70.0, 94.0], [89.5, 6.3, 61.0, 95.0], [92.0, 8.5, 49.0, 96.8],
[93.8, 10.2, 42.0, 97.8], [95.5, 12.8, 35.0, 98.7], [96.4, 14.6, 29.0, 99.2],
[97.1, 16.2, 25.0, 99.5], [98.0, 18.5, 20.0, 99.8]
], dtype=float)

Y = np.array([
18.0, 27.0, 34.0, 42.0, 49.0, 55.0, 61.0, 68.0, 74.0, 81.0, 10.0,
22.0, 31.0, 39.0, 53.0, 64.0, 76.0, 88.0, 95.0, 100.0
], dtype=float)

# 2. Normalisation (Très important pour que l'IA apprenne bien)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Création du modèle
model = Sequential([
    Dense(16, activation='relu', input_shape=(4,)),
    Dense(8, activation='relu'),
    Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])
model.fit(X_scaled, Y, epochs=1000, verbose=0) # verbose=0 cache les 1000 lignes de calcul

# 4. Création du dossier et sauvegarde
os.makedirs('ml_models', exist_ok=True)
model.save('ml_models/modele_qos.h5')
joblib.dump(scaler, 'ml_models/scaler_qos.pkl')

print("✅ SUCCÈS : L'Intelligence Artificielle est prête et sauvegardée dans le dossier 'ml_models' !")