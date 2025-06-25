# Cloud Logging

**Keywords**: `Logging`, `Observabilité`, `Logs`, `Monitoring`, `Alerting`, `GCP`, `Managed Services`, `Audit`, `Stackdriver`

---

## 🧠 Description Générale

**Cloud Logging** (anciennement Stackdriver Logging) est le service de gestion des logs de Google Cloud. Il permet de collecter, stocker, rechercher, analyser et exporter les logs provenant des ressources GCP, AWS ou sur site, pour le monitoring, l’audit et le troubleshooting.

Caractéristiques principales :
- Collecte automatique des logs des services GCP et applications personnalisées.
- Recherche et filtrage avancés via la console ou l’API.
- Export des logs vers BigQuery, Cloud Storage, Pub/Sub.
- Intégration avec Cloud Monitoring pour créer des alertes sur les logs.
- Conservation configurable et gestion des accès fine (IAM).

---

## 🧰 Composants Principaux

### 1. **Log Buckets**
- Espaces de stockage pour organiser et conserver les logs.
- Conservation personnalisable par bucket.

### 2. **Log Sinks**
- Export automatique des logs vers BigQuery, Cloud Storage, Pub/Sub.

### 3. **Log-based Metrics**
- Création de métriques personnalisées à partir des logs pour le monitoring.

### 4. **Alerting**
- Déclenchement d’alertes sur des patterns ou erreurs détectés dans les logs.

### 5. **Audit Logs**
- Journaux d’audit pour la traçabilité des accès et modifications sur les ressources.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Supervision applicative             | Analyse des erreurs et exceptions dans les applications |
| Audit de sécurité                   | Suivi des accès et modifications sur les ressources |
| Export analytique                   | Envoi des logs vers BigQuery pour analyse avancée |
| Déclenchement d’alertes             | Création d’alertes sur des patterns critiques |
| Débogage                            | Recherche rapide dans les logs pour le troubleshooting |

---

## 🧑‍🔬 Exemple d’Architecture : Cloud Logging sur GCP

1. **Sources** : [Compute Engine](../ComputeEngine/computeengine.md), [GKE](../KubernetesEngine/kubernetesengine.md), [App Engine](../AppEngine/appengine.md), etc.
2. **Collecte** : Logs collectés automatiquement ou via API/agents.
3. **Stockage** : Organisation dans des log buckets avec conservation personnalisée.
4. **Export** : Sinks vers [BigQuery](../BigQuery/bigquery.md), [Cloud Storage](../Storage/storage.md), [Pub/Sub](../PubSub/pubsub.md).
5. **Monitoring** : Création de métriques et alertes à partir des logs.

---

# 🚀 Commandes / Code utiles

### Exemple : Écrire un log applicatif en Python

```python
import google.cloud.logging

client = google.cloud.logging.Client()
client.setup_logging()

import logging
logging.info("Ceci est un log d'information envoyé à Cloud Logging.")
```

# Exemple : Créer un sink d'export vers BigQuery

```bash
gcloud logging sinks create my-bq-sink bigquery.googleapis.com/projects/your-project/datasets/your_dataset \
  --log-filter="resource.type=gce_instance"
```

## ✅ Bonnes Pratiques

- Organiser les logs dans des buckets par environnement ou application.
- Configurer la conservation selon les besoins de conformité.
- Exporter les logs critiques vers BigQuery ou Cloud Storage pour l’archivage.
- Créer des alertes sur les erreurs ou patterns critiques.
- Limiter les accès aux logs sensibles via IAM.