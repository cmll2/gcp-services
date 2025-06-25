# Dataproc

**Keywords**: `Hadoop`, `Spark`, `Big Data`, `Cluster`, `Managed`, `ETL`, `Data Lake`, `GCP`, `Serverless`, `Analytics`

---

## 🧠 Description Générale

**Dataproc** est un service managé de Google Cloud pour le déploiement, la gestion et le scaling de clusters Apache Hadoop, Spark, Hive et d’autres outils Big Data. Il permet d’exécuter des traitements de données massifs de façon flexible et économique.

Caractéristiques principales :
- Création et suppression rapide de clusters à la demande.
- Facturation à la seconde, scaling automatique.
- Intégration native avec Cloud Storage, BigQuery, Cloud Logging, etc.
- Support des jobs Spark, Hadoop, Hive, Presto, PySpark, etc.
- Gestion simplifiée des dépendances et des configurations.

---

## 🧰 Composants Principaux

### 1. **Clusters**
- Groupes de VM configurées pour exécuter des workloads Big Data.
- Personnalisation des ressources (CPU, RAM, disques, nombre de nœuds).

### 2. **Jobs**
- Exécution de traitements Spark, Hadoop, Hive, PySpark, etc.
- Soumission via CLI, API, ou interface web.

### 3. **Autoscaling**
- Ajustement automatique du nombre de nœuds selon la charge.

### 4. **Intégration GCP**
- Connexion directe à Cloud Storage, BigQuery, Cloud Logging, Cloud Monitoring.

### 5. **Initialisation & Scripts**
- Scripts d’initialisation pour installer des dépendances ou configurer le cluster.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| ETL Big Data                        | Traitement et transformation de gros volumes de données |
| Machine Learning distribué          | Entraînement de modèles ML sur Spark |
| Data Lake                           | Préparation et analyse de données non structurées |
| Migration Hadoop                    | Déplacement de workloads Hadoop on-premise vers le cloud |
| Analyse ad hoc                      | Exécution ponctuelle de jobs analytiques |

---

## 🧑‍🔬 Exemple d’Architecture : Dataproc sur GCP

1. **Stockage** : Données sources sur [Cloud Storage](../Storage/storage.md).
2. **Cluster Dataproc** : Création à la demande pour exécuter les jobs.
3. **Traitement** : Jobs Spark/Hadoop/PySpark soumis au cluster.
4. **Sortie** : Résultats stockés sur Cloud Storage ou [BigQuery](../BigQuery/bigquery.md).
5. **Monitoring** : Supervision via [Cloud Monitoring](../CloudMonitoring/cloudmonitoring.md) et [Cloud Logging](../CloudLogging/cloudlogging.md).

---

# 🚀 Commandes / Code utiles

### Exemple : Créer un cluster Dataproc

```bash
gcloud dataproc clusters create my-cluster \
  --region=europe-west1 \
  --zone=europe-west1-b \
  --single-node \
  --image-version=2.0-debian10
```

### Exemple : Soumettre un job PySpark

```bash
gcloud dataproc jobs submit pyspark gs://your-bucket/scripts/my_job.py \
  --cluster=my-cluster \
  --region=europe-west1
```

## ✅ Bonnes Pratiques

- Créer et supprimer les clusters à la demande pour optimiser les coûts.
- Utiliser Cloud Storage comme data lake pour séparer stockage et calcul.
- Automatiser les jobs avec des workflows ou des scripts d’initialisation.
- Superviser les clusters et jobs avec Cloud Monitoring et Logging.
- Sécuriser l’accès aux données et clusters avec IAM et VPC.
