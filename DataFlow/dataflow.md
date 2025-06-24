# Dataflow

**Keywords**: `ETL`, `Streaming`, `Batch`, `Apache Beam`, `Data Pipelines`, `Serverless`, `GCP`, `Managed Services`

---

## 🧠 Description Générale

**Dataflow** est un service entièrement géré de Google Cloud pour le traitement de données en mode batch et streaming. Basé sur le framework **Apache Beam**, il permet de créer des pipelines de données scalables et performants.

Caractéristiques principales :
- Traitement unifié des données en **batch** et en **streaming**.
- Évolutivité automatique pour gérer des volumes de données variables.
- Intégration avec d'autres services GCP comme Pub/Sub, BigQuery, Cloud Storage.
- Modèle de programmation basé sur Apache Beam.

---

## 🧰 Composants Principaux

### 1. **Pipelines**
- Définissent le flux de données à travers des étapes de transformation.
- Écrits en Python, Java ou SQL via Apache Beam.

### 2. **Sources de données**
- Supporte des sources comme Pub/Sub, Cloud Storage, BigQuery, Kafka, bases de données.

### 3. **Transformations**
- **ParDo** : Transformation élément par élément.
- **GroupByKey** : Regroupement des données par clé.
- **Windowing** : Regroupement des données en fenêtres temporelles.

### 4. **Sinks (Cibles)**
- Export des données transformées vers des destinations comme BigQuery, Cloud Storage, Pub/Sub.

### 5. **Templates**
- Pipelines préconfigurés pour des cas d'usage courants (ETL, migration de données).

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| ETL (Extract, Transform, Load)     | Extraction de données depuis des sources multiples, transformation et chargement dans BigQuery |
| Traitement de logs en temps réel    | Ingestion de logs via Pub/Sub et analyse en streaming |
| Migration de données                | Déplacement de données entre systèmes (Cloud Storage vers BigQuery) |
| Analyse IoT                         | Traitement en temps réel des données IoT via Pub/Sub |
| Détection de fraudes                | Analyse en streaming pour identifier des anomalies dans les transactions |

---

## 🧑‍🔬 Exemple d’Architecture : Pipeline Dataflow

1. **Source de données** : [Pub/Sub](../PubSub/pubsub.md) ou [Cloud Storage](../Storage/storage.md).
2. **Pipeline Dataflow** : Transformations des données avec Apache Beam.
3. **Cible** : [BigQuery](../BigQuery/bigquery.md) ou [Cloud Storage](../Storage/storage.md).
4. **Monitoring** : Supervision des métriques via [Cloud Monitoring](../CloudMonitoring/cloudmonitoring.md).

---

# 🚀 Commandes / Code utiles

### Exemple : Pipeline Dataflow en Python

```python
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

pipeline_options = PipelineOptions(
    project='your-project-id',
    region='us-central1',
    runner='DataflowRunner',
    temp_location='gs://your-bucket/temp',
    staging_location='gs://your-bucket/staging'
)

def transform_data(element):
    # Exemple de transformation
    return element.upper()

with beam.Pipeline(options=pipeline_options) as p:
    (p
     | 'Lire depuis Pub/Sub' >> beam.io.ReadFromPubSub(topic='projects/your-project-id/topics/your-topic')
     | 'Transformer les données' >> beam.Map(transform_data)
     | 'Écrire dans BigQuery' >> beam.io.WriteToBigQuery(
         table='your-project-id:your_dataset.your_table',
         schema='field1:STRING, field2:INTEGER',
         write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
     ))
```

## ✅ Bonnes Pratiques

- Utiliser des fenêtres temporelles pour regrouper les données en streaming.
- Configurer des pipelines templates pour réutiliser des workflows courants.
- Superviser les pipelines avec Cloud Monitoring pour détecter les erreurs.
- Optimiser les coûts en ajustant les paramètres de parallélisme.
- Tester localement avec le DirectRunner avant de déployer sur Dataflow.