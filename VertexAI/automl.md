# AutoML

**Keywords**: `Machine Learning`, `AutoML`, `No Code`, `Custom Models`, `Vision`, `NLP`, `Tabular Data`, `GCP`, `Managed Services`

---

## 🧠 Description Générale

**AutoML** est une suite d'outils de Machine Learning proposée par Google Cloud qui permet de créer des modèles personnalisés sans nécessiter de compétences avancées en ML. Elle automatise des tâches complexes comme la sélection de modèles, l'entraînement et l'optimisation des hyperparamètres.

Caractéristiques principales :
- Création de modèles personnalisés pour des cas d'usage spécifiques.
- Supporte plusieurs types de données : images, texte, données tabulaires, vidéos.
- Interface conviviale (UI) et API pour les utilisateurs avancés.
- Intégration avec d'autres services GCP comme Cloud Storage et BigQuery.

---

## 🧰 Composants Principaux

### 1. **AutoML Vision**
- Entraînement de modèles pour la classification d'images, la détection d'objets et la segmentation d'images.

### 2. **AutoML Natural Language**
- Analyse de texte pour la classification, l'extraction d'entités et l'analyse des sentiments.

### 3. **AutoML Tables**
- Modèles pour les données tabulaires, comme la prédiction de valeurs ou la classification.

### 4. **AutoML Video Intelligence**
- Analyse vidéo pour la détection d'objets et la reconnaissance d'activités.

### 5. **AutoML Translation**
- Création de modèles de traduction personnalisés pour des paires de langues spécifiques.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Classification d'images            | Identifier des catégories dans des images (ex. : produits, animaux) |
| Analyse de sentiments              | Détecter les sentiments dans des avis ou des commentaires |
| Prédiction de ventes               | Utiliser des données tabulaires pour prédire des tendances ou des valeurs |
| Détection d'objets                 | Identifier des objets spécifiques dans des images ou vidéos |
| Traduction personnalisée           | Traduire des textes avec des modèles adaptés à un domaine spécifique |

---

## 🧑‍🔬 Exemple d’Architecture : AutoML Vision

1. **Source de données** : Chargement des images dans un bucket [Cloud Storage](../Storage/storage.md).
2. **Entraînement** : Création et entraînement d'un modèle avec AutoML Vision.
3. **Évaluation** : Analyse des performances du modèle (précision, rappel).
4. **Déploiement** : Déploiement du modèle sur un endpoint pour l'inférence.
5. **Utilisation** : Envoi d'images au modèle via une API REST pour obtenir des prédictions.

---

# 🚀 Commandes / Code utiles

### Exemple : Entraîner un modèle AutoML Tables

```python
from google.cloud import automl_v1beta1 as automl

client = automl.AutoMlClient()

project_id = "your-project-id"
dataset_id = "your-dataset-id"
display_name = "your-model-name"

model = {
    "display_name": display_name,
    "dataset_id": dataset_id,
    "tables_model_metadata": {"train_budget_milli_node_hours": 1000},
}

response = client.create_model(parent=f"projects/{project_id}/locations/us-central1", model=model)
print(f"Modèle en cours de création : {response.operation.name}")
```

## Exemple : Obtenir une prédiction avec un modèle déployé

```python
from google.cloud import automl_v1beta1 as automl

client = automl.PredictionServiceClient()

project_id = "your-project-id"
model_id = "your-model-id"
payload = {"row": {"values": ["value1", "value2", "value3"]}}

name = f"projects/{project_id}/locations/us-central1/models/{model_id}"
response = client.predict(name=name, payload=payload)
print("Prédictions :")
for result in response.payload:
    print(f"Valeur prédite : {result.tables.value}")
```

## ✅ Bonnes Pratiques

- Préparer les données avec soin (nettoyage, étiquetage) pour améliorer les performances du modèle.
- Utiliser des ensembles de données équilibrés pour éviter les biais.
- Tester les modèles avec des données de validation avant de les déployer.
- Superviser les performances des modèles en production avec Model Monitoring.
- Optimiser les coûts en ajustant le budget d'entraînement.