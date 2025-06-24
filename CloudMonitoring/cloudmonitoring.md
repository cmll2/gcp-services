# Cloud Monitoring

**Keywords**: `Observabilité`, `Metrics`, `Logs`, `Dashboards`, `Alerts`, `GCP`, `Managed Services`, `Monitoring`

---

## 🧠 Description Générale

**Cloud Monitoring** (anciennement Stackdriver) est le service de surveillance de Google Cloud. Il permet de collecter, visualiser et alerter sur les métriques et logs des ressources GCP, AWS ou sur site, afin d’assurer la disponibilité et la performance des applications.

Caractéristiques principales :
- Collecte automatique des métriques des ressources GCP.
- Création de dashboards personnalisés et interactifs.
- Configuration d’alertes sur seuils ou conditions complexes.
- Intégration avec Cloud Logging pour l’analyse des logs.
- Support multi-cloud (GCP, AWS, on-premise).
- Intégration avec PagerDuty, Slack, email, SMS, etc.

---

## 🧰 Composants Principaux

### 1. **Metrics**
- Données de performance collectées automatiquement ou via API.
- Exemples : CPU, mémoire, latence, erreurs, métriques personnalisées.

### 2. **Dashboards**
- Visualisation graphique des métriques.
- Tableaux de bord prédéfinis ou personnalisés.

### 3. **Alerting Policies**
- Déclenchement d’alertes selon des règles définies.
- Notifications multi-canaux.

### 4. **Uptime Checks**
- Vérification de la disponibilité des endpoints HTTP/HTTPS, TCP, etc.

### 5. **Logs-Based Metrics**
- Création de métriques personnalisées à partir des logs Cloud Logging.

### 6. **Service Monitoring**
- Vue unifiée des performances et dépendances des services.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Supervision d’infrastructure        | Suivi des VM, bases de données, réseaux |
| Détection d’anomalies               | Alertes sur pics de latence ou erreurs |
| Monitoring applicatif               | Tableaux de bord pour microservices ou APIs |
| Analyse des logs                    | Création de métriques à partir des logs |
| Vérification de disponibilité       | Uptime checks pour endpoints critiques |

---

## 🧑‍🔬 Exemple d’Architecture : Cloud Monitoring sur GCP

1. **Sources** : [Compute Engine](../ComputeEngine/computeengine.md), [GKE](../KubernetesEngine/kubernetesengine.md), [App Engine](../AppEngine/appengine.md), etc.
2. **Collecte** : Métriques et logs collectés automatiquement ou via agents.
3. **Dashboards** : Visualisation dans Cloud Monitoring.
4. **Alertes** : Notifications via email, Slack, PagerDuty, etc.
5. **Actions** : Intégration avec Cloud Functions ou outils d’incident.

---

# 🚀 Commandes / Code utiles

### Exemple : Créer une métrique personnalisée en Python

```python
from google.cloud import monitoring_v3

client = monitoring_v3.MetricServiceClient()
project_name = f"projects/your-project-id"

descriptor = monitoring_v3.MetricDescriptor()
descriptor.type = "custom.googleapis.com/my_custom_metric"
descriptor.metric_kind = monitoring_v3.MetricDescriptor.MetricKind.GAUGE
descriptor.value_type = monitoring_v3.MetricDescriptor.ValueType.DOUBLE
descriptor.description = "Une métrique personnalisée pour le suivi des performances."

descriptor = client.create_metric_descriptor(name=project_name, metric_descriptor=descriptor)
print(f"Créé la métrique personnalisée : {descriptor.name}")
```

Exemple : Créer une alerte sur une métrique

- Depuis la console GCP : Monitoring > Alertes > Créer une politique d’alerte.
- Ou via Terraform, API, etc.

## ✅ Bonnes Pratiques

- Créer des dashboards partagés pour la visibilité d’équipe.
- Configurer des alertes proactives sur les métriques critiques.
- Utiliser des logs-based metrics pour des analyses avancées.
- Surveiller les coûts liés à la collecte de métriques/logs.
- Intégrer le monitoring dans les workflows d’incident (PagerDuty, Slack…).