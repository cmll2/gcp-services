# Apache Hadoop

**Keywords**: `Big Data`, `HDFS`, `MapReduce`, `YARN`, `Distributed Computing`, `Batch`, `Open Source`, `Data Lake`, `Cluster`

---

## 🧠 Description Générale

**Apache Hadoop** est un framework open source pour le stockage et le traitement distribué de très grands volumes de données. Il repose sur un système de fichiers distribué (HDFS) et un moteur de calcul batch (MapReduce), orchestrés par YARN.

Caractéristiques principales :
- Stockage distribué et tolérant aux pannes via HDFS.
- Traitement batch massif avec MapReduce.
- Orchestration des ressources et des jobs via YARN.
- Écosystème riche : Hive, Pig, HBase, Spark, Oozie, etc.
- Déploiement sur clusters on-premise ou cloud (ex : Dataproc, EMR).

---

## 🧰 Composants Principaux

### 1. **HDFS (Hadoop Distributed File System)**
- Système de fichiers distribué, stockage redondant et scalable.

### 2. **MapReduce**
- Modèle de programmation pour le traitement batch distribué.

### 3. **YARN (Yet Another Resource Negotiator)**
- Gestion des ressources et orchestration des jobs sur le cluster.

### 4. **Écosystème Hadoop**
- Outils complémentaires : Hive (SQL), Pig (scripts), HBase (NoSQL), Oozie (workflow), Spark (traitement en mémoire), etc.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| ETL Big Data                        | Traitement batch de gros volumes de données |
| Data Lake                           | Stockage et préparation de données non structurées |
| Machine Learning distribué          | Préparation de données pour Spark/MLlib |
| Archivage massif                    | Stockage longue durée de données brutes |
| Migration cloud                     | Déploiement sur Dataproc, EMR, HDInsight |

---

## 🧑‍🔬 Exemple d’Architecture : Hadoop sur cluster

1. **Stockage** : Données sur HDFS, ingestion depuis bases, fichiers, IoT, etc.
2. **Traitement** : Jobs MapReduce ou Spark soumis au cluster.
3. **Orchestration** : YARN gère la répartition des ressources et l’exécution des jobs.
4. **Sortie** : Résultats stockés sur HDFS, exportés vers bases ou data marts.
5. **Surveillance** : Monitoring via outils natifs ou intégration avec Prometheus, Grafana.

---

# 🚀 Commandes / Code utiles

### Exemple : Lancer un job MapReduce

```bash
hadoop jar /path/to/hadoop-examples.jar wordcount /input /output
```

## ✅ Bonnes Pratiques

- Répliquer les données (par défaut x3) pour la tolérance aux pannes.
- Surveiller l’espace disque et la santé du cluster.
- Utiliser YARN pour optimiser l’allocation des ressources.
- Automatiser les workflows avec Oozie ou Airflow.
- Sécuriser l’accès avec Kerberos et les ACLs HDFS.
- Privilégier Spark pour les traitements interactifs ou en mémoire.