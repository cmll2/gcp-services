# Cloud Storage

**Keywords**: `Object Storage`, `Buckets`, `Files`, `Scalable`, `Serverless`, `GCP`, `Managed Services`, `Backup`

---

## 🧠 Description Générale

**Cloud Storage** est un service de stockage d'objets entièrement géré et scalable proposé par Google Cloud. Il permet de stocker des fichiers de tout type et de toute taille, avec des options de durabilité, de sécurité et de performance adaptées à divers cas d'usage.

Caractéristiques principales :
- Stockage illimité pour des fichiers de tout type.
- Classes de stockage adaptées aux besoins (Standard, Nearline, Coldline, Archive).
- Intégration avec d'autres services GCP comme BigQuery, Dataflow, Pub/Sub.
- Sécurité avancée avec gestion des accès et chiffrement des données.
- Haute disponibilité et durabilité (99.999999999% de durabilité).

---

## 🧰 Composants Principaux

### 1. **Buckets**
- Conteneurs pour stocker les objets.
- Configurations possibles :
  - Région unique, multi-région ou dual-région.
  - Classes de stockage (Standard, Nearline, Coldline, Archive).
  - Gestion des versions pour conserver les anciennes versions des objets.

### 2. **Objets**
- Fichiers stockés dans les buckets.
- Métadonnées associées pour décrire les fichiers.

### 3. **ACL et IAM**
- Contrôle des accès via des listes de contrôle d'accès (ACL) ou des rôles IAM.

### 4. **Lifecycle Management**
- Règles pour automatiser la transition des objets entre classes de stockage ou leur suppression.

### 5. **Signed URLs et Signed Policy Documents**
- Accès temporaire aux objets via des URLs signées.

### 6. **Notifications**
- Intégration avec Pub/Sub pour déclencher des événements lors de modifications dans les buckets.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Stockage de fichiers statiques      | Hébergement de fichiers comme des images, vidéos ou backups |
| Archivage                           | Stockage à long terme avec les classes Coldline ou Archive |
| Analyse de données                  | Stockage des fichiers source pour traitement avec BigQuery ou Dataflow |
| Distribution de contenu             | Utilisation avec un CDN pour diffuser des fichiers à faible latence |
| Sauvegarde et reprise après sinistre| Stockage des backups critiques avec durabilité élevée |

---

## 🧑‍🔬 Exemple d’Architecture : Cloud Storage pour ETL

1. **Source de données** : Chargement des fichiers dans un bucket Cloud Storage.
2. **Pipeline de traitement** : Utilisation de [Dataflow](../Dataflow/dataflow.md) pour transformer les données.
3. **Destination** : Export des données transformées vers [BigQuery](../BigQuery/bigquery.md) ou un autre bucket.
4. **Monitoring** : Notifications via [Pub/Sub](../PubSub/pubsub.md) pour surveiller les modifications dans les buckets.

---

# 🚀 Commandes / Code utiles

### Exemple : Création d'un bucket

```python
from google.cloud import storage

client = storage.Client()
bucket_name = "your-bucket-name"

bucket = client.create_bucket(bucket_name)
print(f"Bucket {bucket.name} créé avec succès.")
```

### Exemple : Téléchargement d'un fichier dans un bucket

```python
from google.cloud import storage

client = storage.Client()
bucket_name = "your-bucket-name"
source_file_name = "local-file.txt"
destination_blob_name = "uploaded-file.txt"

bucket = client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)

blob.upload_from_filename(source_file_name)
print(f"Fichier {source_file_name} téléchargé dans le bucket {bucket_name} sous le nom {destination_blob_name}.")
```

## ✅ Bonnes Pratiques
- Utiliser des classes de stockage adaptées aux besoins pour optimiser les coûts.
- Activer la gestion des versions pour éviter la perte accidentelle de données.
- Configurer des règles de cycle de vie pour automatiser la gestion des objets.
- Utiliser des Signed URLs pour partager des fichiers de manière sécurisée.
- Superviser les accès et les modifications avec Cloud Monitoring et Cloud Logging.