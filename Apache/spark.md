# Apache Spark

**Keywords**: `Big Data`, `Spark`, `Distributed Computing`, `Batch`, `Streaming`, `ETL`, `Machine Learning`, `Analytics`, `Open Source`, `Cluster`

---

## 🧠 Description Générale

**Apache Spark** est un moteur open source de traitement distribué pour le Big Data. Il permet d’exécuter des traitements batch, du streaming, du machine learning et de l’analytique avancée sur de grands volumes de données, en mémoire ou sur disque.

Caractéristiques principales :
- Traitement distribué en mémoire pour des performances élevées.
- Support du batch, du streaming, du ML (MLlib) et du SQL (Spark SQL).
- API unifiées en Python (PySpark), Scala, Java, R.
- Intégration avec HDFS, S3, Hive, Cassandra, HBase, etc.
- Déploiement sur clusters on-premise, cloud, Kubernetes, YARN, Mesos.

---

## 🧰 Composants Principaux

### 1. **Spark Core**
- Moteur d’exécution distribué, gestion des tâches et de la mémoire.

### 2. **Spark SQL**
- Requêtes SQL, DataFrames, intégration avec Hive Metastore.

### 3. **Spark Streaming**
- Traitement de flux de données en temps réel (micro-batching).

### 4. **MLlib**
- Librairie de machine learning distribuée (classification, clustering, régression…).

### 5. **GraphX**
- Traitement de graphes distribués.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| ETL Big Data                        | Préparation et transformation de données massives |
| Streaming temps réel                | Analyse de flux (logs, IoT, clickstream…) |
| Machine Learning distribué          | Entraînement de modèles ML sur de gros volumes |
| SQL analytique                      | Requêtes SQL sur des data lakes |
| Traitement de graphes               | Analyse de réseaux sociaux, recommandations |

---

## 🧑‍🔬 Exemple d’Architecture : Spark sur cluster

1. **Stockage** : Données sur HDFS, S3, Cloud Storage, etc.
2. **Cluster Spark** : Déploiement sur YARN, Kubernetes, Dataproc, EMR, etc.
3. **Traitement** : Jobs Spark batch ou streaming soumis au cluster.
4. **Sortie** : Résultats sur HDFS, S3, BigQuery, bases SQL, etc.
5. **Monitoring** : Suivi via Spark UI, Cloud Monitoring, Prometheus, Grafana.

---

# 🚀 Commandes / Code utiles

### Exemple : Lancer un job PySpark

```bash
spark-submit --master yarn --deploy-mode cluster my_job.py
```

### Exemple : Traitement de données avec PySpark

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()
df = spark.read.csv("s3://my-bucket/data.csv", header=True, inferSchema=True)
df.groupBy("category").count().show()
```

### Exemple : Streaming avec PySpark

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("streaming").getOrCreate()
df = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
df.writeStream.format("console").start().awaitTermination()
```

## ✅ Bonnes Pratiques

- Utiliser le partitionnement et le cache pour optimiser les performances.
- Superviser les jobs avec Spark UI et des outils externes.
- Gérer les dépendances avec des fichiers requirements ou jars.
- Adapter le nombre de partitions à la taille des données.
- Nettoyer les ressources (jobs, clusters) après usage pour maîtriser les coûts.
- Privilégier DataFrames/Datasets pour les traitements complexes.

