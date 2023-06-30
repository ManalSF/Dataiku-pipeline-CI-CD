import pandas as pd

# Lecture des données
data = pd.read_csv('data/Defects_On_Production_lines_train.csv')

# Élimination des doublons
data = data.drop_duplicates()

# Élimination des valeurs manquantes
data = data.dropna()

# Sauvegarde des données prétraitées
data.to_csv('data/Defects_On_Production_lines_preprocessed.csv', index=False)
