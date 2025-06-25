# Apache Hive

**Keywords**: `Big Data`, `SQL`, `Data Warehouse`, `Hadoop`, `ETL`, `Batch`, `Schema-on-Read`, `Open Source`, `Analytics`

---

## 🧠 Description Générale

**Apache Hive** est un système d’entrepôt de données open source conçu pour interroger et analyser de grands volumes de données stockés dans Hadoop. Il permet d’utiliser un langage proche du SQL (HiveQL) pour effectuer des requêtes, des analyses et des transformations sur des données distribuées.

Caractéristiques principales :
- Requêtes SQL (HiveQL) sur des données stockées dans HDFS, S3, etc.
- Exécution des requêtes via MapReduce, Tez ou Spark.
- Gestion de schémas (schema-on-read) et de tables partitionnées.
- Support des UDF/UDAF pour des traitements personnalisés.
- Intégration avec l’écosystème Hadoop (HDFS, YARN, Oozie, etc.).

---

## 🧰 Composants Principaux

### 1. **Metastore**
- Base de données centralisant les métadonnées des tables, partitions, schémas.

### 2. **HiveQL**
- Langage de requête similaire à SQL, adapté au Big Data.

### 3. **Drivers d’exécution**
- MapReduce, Tez, Spark : moteurs pour exécuter les requêtes HiveQL.

### 4. **Tables et partitions**
- Tables internes ou externes, partitionnement pour optimiser les requêtes.

### 5. **UDF/UDAF**
- Fonctions personnalisées pour enrichir les traitements.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Data Warehouse Big Data             | Entrepôt analytique sur HDFS ou S3 |
| ETL batch                           | Transformation et préparation de données massives |
| Reporting analytique                | Génération de rapports sur de gros volumes de données |
| Migration SQL vers Hadoop           | Utilisation de SQL sur des données distribuées |
| Exploration de Data Lake            | Analyse ad hoc sur des données brutes |

---

## 🧑‍🔬 Exemple d’Architecture : Hive sur Hadoop

1. **Stockage** : Données sur HDFS ou S3.
2. **Metastore** : Métadonnées centralisées (MySQL, PostgreSQL, etc.).
3. **Traitement** : Requêtes HiveQL exécutées via MapReduce, Tez ou Spark.
4. **Orchestration** : Workflows automatisés avec Oozie ou Airflow.
5. **Sortie** : Résultats stockés sur HDFS, S3 ou exportés vers d’autres systèmes.

---

# 🚀 Commandes / Code utiles

### Exemple : Lancer le shell Hive

```bash
hive
```

### Exemple : Créer une table Hive

```sql
CREATE TABLE ventes (
  id INT,
  produit STRING,
  montant DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

## ✅ Bonnes Pratiques

- Utiliser le partitionnement pour accélérer les requêtes sur de gros volumes.
- Centraliser les métadonnées dans un Metastore robuste.
- Privilégier Tez ou Spark pour des performances accrues.
- Documenter les schémas et les UDF/UDAF personnalisées.
- Sécuriser l’accès au Metastore et aux données (Kerberos, ACLs).
- Nettoyer régulièrement les tables temporaires et les partitions obsolètes.