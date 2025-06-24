# Cloud SQL

**Keywords**: `Database`, `SQL`, `Managed`, `PostgreSQL`, `MySQL`, `SQL Server`, `Backup`, `High Availability`, `GCP`

---

## 🧠 Description Générale

**Cloud SQL** est un service de base de données relationnelle entièrement géré par Google Cloud. Il prend en charge les moteurs **PostgreSQL**, **MySQL** et **SQL Server**, et permet de déployer, gérer et scaler des bases de données SQL sans gestion d’infrastructure.

Caractéristiques principales :
- Provisionnement, sauvegarde et restauration automatisés.
- Haute disponibilité avec basculement automatique.
- Mise à l’échelle verticale et horizontale.
- Sécurité avancée (chiffrement, IAM, VPC).
- Intégration avec d’autres services GCP (BigQuery, Dataflow, App Engine).

---

## 🧰 Composants Principaux

### 1. **Instances**
- Serveurs de bases de données gérés (PostgreSQL, MySQL, SQL Server).
- Configuration des ressources (CPU, RAM, stockage).

### 2. **Bases de données**
- Création et gestion de bases de données à l’intérieur d’une instance.

### 3. **Utilisateurs et accès**
- Gestion des comptes utilisateurs SQL et des permissions.
- Intégration IAM pour le contrôle d’accès.

### 4. **Sauvegardes et restauration**
- Sauvegardes automatiques et manuelles.
- Restauration à un instant T (point-in-time recovery).

### 5. **Haute disponibilité**
- Réplication synchrone, basculement automatique, adresses IP privées.

### 6. **Surveillance et alertes**
- Intégration avec Cloud Monitoring et Cloud Logging.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Application web transactionnelle    | Backend SQL pour applications web ou mobiles |
| Migration de bases de données       | Déplacement de bases existantes vers le cloud |
| Analytics temps réel                | Connexion à BigQuery ou Dataflow pour analyse |
| Sauvegarde et reprise après sinistre| Sauvegardes automatiques et restauration rapide |
| Multi-cloud ou hybride              | Connexion sécurisée depuis d’autres clouds ou sur site |

---

## 🧑‍🔬 Exemple d’Architecture : Cloud SQL avec GCP

1. **Application** : [App Engine](../Engines/appengine.md), [Compute Engine](../Engines/computeengine.md) ou [Kubernetes Engine](../Engines/kubernetesengine.md)
2. **Base de données** : Instance Cloud SQL (PostgreSQL/MySQL/SQL Server)
3. **Sauvegardes** : Automatiques et stockées dans Cloud Storage
4. **Surveillance** : [Cloud Monitoring](../CloudMonitoring/cloudmonitoring.md)
5. **Analytics** : Export vers [BigQuery](../BigQuery/bigquery.md) pour analyse avancée

---

# 🚀 Commandes / Code utiles

### Exemple : Connexion à Cloud SQL en Python (PostgreSQL)

```python
import sqlalchemy

db_user = "user"
db_pass = "password"
db_name = "database"
cloud_sql_connection_name = "project:region:instance"

# Pour une connexion via le proxy Cloud SQL
db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL.create(
        drivername="postgresql+pg8000",
        username=db_user,
        password=db_pass,
        database=db_name,
        query={
            "unix_sock": f"/cloudsql/{cloud_sql_connection_name}/.s.PGSQL.5432"
        },
    ),
)

with db.connect() as conn:
    result = conn.execute("SELECT NOW()")
    print(result.fetchone())
```

### Exemple : Sauvegarde manuelle via gcloud

```bash
gcloud sql backups create --instance=your-instance-name
```

### Exemple : Restauration d’une sauvegarde

```bash
gcloud sql backups restore BACKUP_ID --instance=your-instance-name --restore-instance=your-instance-name
``` 

## ✅ Bonnes Pratiques

- Activer la haute disponibilité pour les environnements critiques.
- Planifier des sauvegardes automatiques et tester la restauration régulièrement.
- Utiliser des adresses IP privées pour sécuriser les connexions.
- Surveiller les performances avec Cloud Monitoring.
- Limiter les accès avec IAM et les comptes SQL.
- Mettre à jour régulièrement les versions des moteurs SQL.