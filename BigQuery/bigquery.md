# BigQuery

**Keywords**: `Data Warehouse`, `Analytics`, `SQL`, `ETL`, `Serverless`, `Managed Services`, `BI`

---

## 🧠 Description Générale

**BigQuery** est un entrepôt de données entièrement géré et serverless proposé par Google Cloud. Il permet d'exécuter des requêtes SQL analytiques sur des volumes massifs de données en quelques secondes.

Caractéristiques principales :
- Analyse rapide et évolutive.
- Modèle de tarification basé sur l'utilisation (paiement à la requête ou forfait).
- Intégration avec des outils BI comme Looker, Tableau, Data Studio.
- Support des données structurées et semi-structurées (JSON, Avro, Parquet).

---

## 🧰 Composants Principaux

### 1. **Tables et Schémas**
- Stockage des données dans des tables partitionnées ou non.
- Supporte les formats CSV, JSON, Avro, Parquet, ORC.

### 2. **SQL Standard**
- Langage SQL standardisé pour les requêtes.
- Supporte les fonctions analytiques, les jointures complexes, les sous-requêtes.

### 3. **BigQuery ML**
- Entraînement de modèles ML directement avec SQL.
- Modèles supportés : régression, classification, clustering, séries temporelles.

### 4. **BigQuery BI Engine**
- Moteur en mémoire pour des tableaux de bord interactifs.
- Optimisé pour les outils BI.

### 5. **BigQuery Omni**
- Analyse des données stockées sur AWS ou Azure sans les déplacer.

### 6. **Streaming**
- Ingestion en temps réel des données via l'API de streaming.

### 7. **BigQuery Data Transfer Service**
- Automatisation des imports de données depuis des sources comme Google Ads, YouTube, etc.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Analyse des ventes                 | Requêtes SQL sur des données transactionnelles |
| Reporting BI                       | Intégration avec Looker ou Data Studio |
| Analyse de logs                    | Ingestion de logs en temps réel via Cloud Logging |
| Prédiction de tendances            | BigQuery ML pour séries temporelles |
| Analyse multi-cloud                | BigQuery Omni pour AWS/Azure |
| Détection d'anomalies              | Clustering avec BigQuery ML |

---

## 🧑‍🔬 Exemple d’Architecture : Analyse avec BigQuery

1. **Source de données** : [Cloud Storage](../CloudStorage/cloudstorage.md) ou [Pub/Sub](../PubSub/pubsub.md)
2. **Ingestion** : [Dataflow](../Dataflow/dataflow.md) ou API de streaming
3. **Stockage** : Tables BigQuery partitionnées
4. **Analyse** : SQL ou BigQuery ML
5. **Visualisation** : [Looker](../Looker/looker.md) ou [Data Studio](../DataStudio/datastudio.md)

---

# 🚀 Commandes / Code utiles

### Exemple : Requête SQL simple

```sql
SELECT
  customer_id,
  SUM(total_amount) AS total_spent
FROM
  `project_id.dataset_id.sales`
WHERE
  transaction_date BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY
  customer_id
ORDER BY
  total_spent DESC
LIMIT 10;
```

### Exemple : Chargement de données depuis Cloud Storage

```python
from google.cloud import bigquery

client = bigquery.Client()

table_id = "your-project.your_dataset.your_table"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
)

uri = "gs://your-bucket-name/your-file.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)

load_job.result()

print(f"Table {table_id} chargée avec succès.")
```

## ✅ Bonnes Pratiques

- Partitionner les tables pour optimiser les performances.
- Utiliser des clusters pour accélérer les requêtes sur des colonnes spécifiques.
- Activer les quotas et les budgets pour éviter les dépassements de coûts.
- Automatiser les imports avec BigQuery Data Transfer Service.
- Utiliser BigQuery ML pour des analyses prédictives rapides.