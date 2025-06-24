# Vertex AI

**Keywords**: `ML`, `AutoML`, `Custom Training`, `MLOps`, `Pipelines`, `Model Registry`, `Explainable AI`, `Serverless`, `GCP`, `Managed Services`

---

## 🧠 Description Générale

**Vertex AI** est la plateforme de Machine Learning unifiée de Google Cloud. Elle permet de gérer **l’ensemble du cycle de vie ML**, de l’ingestion de données jusqu’à l’inférence, le monitoring, et le réentraînement.

Elle intègre de manière cohérente :
- AutoML
- Entraînement personnalisé
- Déploiement de modèles
- Pipelines (ML workflows)
- Feature Store
- Registry (catalogue de modèles)
- Monitoring des modèles
- Explainable AI (XAI)

---

## 🧰 Composants Principaux

### 1. **AutoML**
- Entraînement automatique de modèles (vision, NLP, tabulaire).
- Aucune expertise ML requise.
- Optimisation automatique de l’architecture + hyperparamètres.

### 2. **Custom Training**
- Utilisation de frameworks comme TensorFlow, PyTorch, XGBoost, scikit-learn.
- Supporte :
  - Entraînement distribué
  - GPU/TPU
  - Jobs Dockerisés (`custom containers`)
- Stockage des artefacts dans Cloud Storage.

### 3. **Vertex AI Workbench**
- Environnement Jupyter géré pour le prototypage.
- Intégré avec BigQuery, Dataflow, Spark, GCS.
- Possibilité de démarrer des notebooks "user-managed" ou "serverless".

### 4. **Pipelines**
- Basés sur Kubeflow Pipelines.
- Orchestration d'étapes ML (prétraitement, entraînement, validation, déploiement).
- Reproductibles, versionnés, auditables.

### 5. **Feature Store**
- Stocke, partage et versionne les features.
- Utilisable à l’entraînement et à l’inférence pour cohérence.

### 6. **Model Registry**
- Catalogue de modèles versionnés.
- Intègre validation, audit, promotion vers staging/prod.

### 7. **Model Monitoring**
- Surveille le drift de données, la performance modèle.
- Alertes automatiques.

### 8. **Explainable AI**
- Génère des explications locales/globales.
- Méthodes : SHAP, Integrated Gradients, etc.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Classification d'images            | AutoML Vision ou modèle TensorFlow personnalisé |
| Détection de fraude                | Pipelines + modèles XGBoost sur données tabulaires |
| Prédiction de churn                | AutoML Tables + Feature Store |
| Analyse de sentiments              | AutoML Text ou fine-tuning BERT |
| Recommandation de contenu          | Entraînement PyTorch + Feature Store |
| Détection d’anomalies industrielles| Custom training + GPU/TPU + déploiement scalable |

---

## 🧑‍🔬 Exemple d’Architecture : Pipeline Vertex AI


[BigQuery](../BigQuery/bigquery.md) (source data)

[Dataflow](../Dataflow/dataflow.md) (ETL)

Vertex AI Training Job (AutoML ou Custom)

[Model-Registry](modelregistry.md) (Model Versioning)

Model Deployment (Endpoint)

Model Monitoring & Retraining Loop


# 🚀 Commandes / Code utiles
Lancer un job de training custom (Python)


```python
from google.cloud import aiplatform

aiplatform.init(project='your-project', location='us-central1')

job = aiplatform.CustomTrainingJob(
    display_name='my-model-training',
    script_path='train.py',
    container_uri='gcr.io/cloud-aiplatform/training/tf-cpu.2-11:latest',
    requirements=['pandas', 'scikit-learn'],
)

model = job.run(
    replica_count=1,
    model_display_name='my-trained-model',
)
Créer un endpoint & déployer un modèle
python
Copier
Modifier
endpoint = model.deploy(machine_type='n1-standard-4')
```

## ✅ Bonnes Pratiques

Toujours versionner les datasets avec des identifiants horodatés

Utiliser Feature Store pour la cohérence entraînement/inférence

Prévoir des pipelines reproductibles (Vertex Pipelines)

Intégrer Model Monitoring dès le départ

Utiliser custom containers pour le contrôle maximal

Activer Explainable AI pour les cas sensibles (finance, santé)