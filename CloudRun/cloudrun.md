# Cloud Run

**Keywords**: `Serverless`, `Containers`, `Microservices`, `HTTP`, `Autoscaling`, `CI/CD`, `GCP`, `Managed Services`, `Stateless`

---

## 🧠 Description Générale

**Cloud Run** est un service serverless de Google Cloud qui permet de déployer et d’exécuter des conteneurs Docker en réponse à des requêtes HTTP. Il gère automatiquement le scaling, la haute disponibilité et la gestion de l’infrastructure, permettant de se concentrer sur le code.

Caractéristiques principales :
- Déploiement de conteneurs stateless en quelques secondes.
- Mise à l’échelle automatique (jusqu’à zéro).
- Facturation à la demande, selon l’utilisation réelle.
- Support de n’importe quel langage ou framework (tant que packagé en conteneur).
- Intégration avec Cloud Build, Artifact Registry, Pub/Sub, IAM, VPC, etc.
- Gestion des révisions et du traffic splitting.

---

## 🧰 Composants Principaux

### 1. **Services**
- Unité de déploiement et de gestion d’un conteneur.
- Chaque service peut avoir plusieurs révisions.

### 2. **Révisions**
- Version immuable d’un service Cloud Run.
- Permet le rollback et le traffic splitting.

### 3. **Traffic Splitting**
- Répartition du trafic entre plusieurs révisions pour tests ou migration progressive.

### 4. **Authentification & IAM**
- Contrôle d’accès fin (public, privé, par identité de service).

### 5. **Variables d’environnement & secrets**
- Injection de variables d’environnement et intégration avec Secret Manager.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| API REST stateless                  | Déploiement rapide d’APIs HTTP |
| Microservices                       | Architecture modulaire et scalable |
| Traitement d’événements             | Consommation d’événements Pub/Sub ou Cloud Tasks |
| Backend d’applications mobiles/web  | Backend scalable et sécurisé |
| Tâches ponctuelles                  | Exécution de jobs courts ou batchs |

---

## 🧑‍🔬 Exemple d’Architecture : Cloud Run sur GCP

1. **Build** : Création d’une image Docker avec [Cloud Build](../CloudBuild/cloudbuild.md).
2. **Stockage** : Image stockée dans [Artifact Registry](../ArtifactRegistry/artifactregistry.md).
3. **Déploiement** : Déploiement de l’image sur Cloud Run.
4. **Intégration** : Connexion à [Pub/Sub](../PubSub/pubsub.md), [Cloud SQL](../SQL/sql.md), [Secret Manager](../SecretManager/secretmanager.md).
5. **Monitoring** : Supervision via [Cloud Monitoring](../CloudMonitoring/cloudmonitoring.md) et [Cloud Logging](../CloudLogging/cloudlogging.md).

---

# 🚀 Commandes / Code utiles

### Exemple : Déployer une image sur Cloud Run

```bash
gcloud run deploy my-service \
  --image=eu.gcr.io/your-project/my-image:latest \
  --platform=managed \
  --region=europe-west1 \
  --allow-unauthenticated
```

### Exemple : Appeler un service Cloud Run

```bash
curl https://my-service-abcdef.a.run.app/endpoint
```

### Exemple : Déployer une image depuis Artifact Registry

```bash
gcloud run deploy my-service \
  --image=europe-west1-docker.pkg.dev/your-project/my-repo/my-image:tag \
  --platform=managed \
  --region=europe-west1
```

## ✅ Bonnes Pratiques

- Utiliser des images légères et sécurisées (multi-stage builds, scan de vulnérabilités).
- Gérer les secrets via Secret Manager et variables d’environnement.
- Restreindre l’accès public si besoin (IAM).
- Superviser les logs et métriques avec Cloud Monitoring/Logging.
- Utiliser le traffic splitting pour les déploiements progressifs.
- Automatiser les builds et déploiements avec Cloud Build et CI/CD.