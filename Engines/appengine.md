# App Engine

**Keywords**: `Serverless`, `PaaS`, `Web Apps`, `Autoscaling`, `Managed`, `GCP`, `Python`, `Java`, `Node.js`, `Flexible`, `Standard`

---

## 🧠 Description Générale

**App Engine** est une plateforme serverless (PaaS) de Google Cloud permettant de déployer des applications web et APIs sans gérer l’infrastructure. Elle prend en charge plusieurs langages (Python, Java, Node.js, Go, PHP, Ruby, .NET) et propose deux environnements : Standard et Flexible.

Caractéristiques principales :
- Déploiement rapide d’applications web et APIs.
- Mise à l’échelle automatique selon la charge.
- Gestion automatique des patchs, sécurité et disponibilité.
- Intégration avec Cloud SQL, Memorystore, Firestore, etc.
- Monitoring et logging intégrés.

---

## 🧰 Composants Principaux

### 1. **Environnement Standard**
- Supporte plusieurs langages avec des runtimes gérés.
- Démarrage rapide, scaling à zéro, facturation à la demande.

### 2. **Environnement Flexible**
- Supporte des conteneurs personnalisés et plus de ressources.
- Basé sur des VM Compute Engine, scaling horizontal.

### 3. **Services & Versions**
- Une application peut contenir plusieurs services (microservices).
- Chaque service peut avoir plusieurs versions déployées.

### 4. **Traffic Splitting**
- Répartition du trafic entre différentes versions pour tests ou migration progressive.

### 5. **Sécurité & IAM**
- Contrôle d’accès fin, intégration avec IAM, gestion des secrets.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Applications web stateless          | Déploiement rapide d’applications web |
| APIs REST                           | Backend serverless pour applications mobiles/web |
| Microservices                       | Architecture multi-services avec gestion du trafic |
| Prototypage rapide                  | Déploiement de MVPs ou de POCs |
| Traitement asynchrone               | Tâches en arrière-plan avec Task Queues ou Cron |

---

## 🧑‍🔬 Exemple d’Architecture : App Engine sur GCP

1. **Code source** : Stocké sur [Cloud Source Repositories](../CloudSourceRepositories/cloudsourcerepositories.md) ou GitHub.
2. **Déploiement** : Application déployée sur App Engine (standard ou flexible).
3. **Base de données** : Connexion à [Cloud SQL](../SQL/sql.md), [Firestore](../Firestore/firestore.md), etc.
4. **Stockage** : Utilisation de [Cloud Storage](../Storage/storage.md).
5. **Monitoring** : Supervision via [Cloud Monitoring](../CloudMonitoring/cloudmonitoring.md) et [Cloud Logging](../CloudLogging/cloudlogging.md).

---

# 🚀 Commandes / Code utiles

### Exemple : Déployer une application

```bash
gcloud app deploy
```

### Exemple : Consulter les logs

```bash
gcloud app logs tail -s default
```

### Exemple : Split du trafic entre deux versions

```bash
gcloud app services set-traffic default --splits v1=0.5,v2=0.5
```

## ✅ Bonnes Pratiques

- Utiliser l’environnement Standard pour les apps web classiques, Flexible pour les besoins spécifiques (conteneurs, ressources).
- Séparer les services pour une architecture modulaire.
- Gérer les secrets via Secret Manager ou variables d’environnement.
- Activer le scaling automatique pour optimiser les coûts.
- Superviser les performances et erreurs avec Cloud Monitoring et Logging.
- Utiliser le traffic splitting pour les déploiements progressifs.