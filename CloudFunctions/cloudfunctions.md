# Cloud Functions

**Keywords**: `Serverless`, `FaaS`, `Event-Driven`, `Microservices`, `HTTP`, `Pub/Sub`, `GCP`, `Managed Services`, `Stateless`, `Automation`

---

## 🧠 Description Générale

**Cloud Functions** est un service serverless (FaaS) de Google Cloud qui permet d’exécuter du code en réponse à des événements, sans gérer d’infrastructure. Il supporte plusieurs langages (Node.js, Python, Go, Java, etc.) et s’intègre nativement avec les autres services GCP.

Caractéristiques principales :
- Déclenchement par événements (HTTP, Pub/Sub, Cloud Storage, Firestore, etc.).
- Mise à l’échelle automatique selon la charge (jusqu’à zéro).
- Facturation à l’utilisation réelle (durée d’exécution, nombre d’appels).
- Déploiement rapide via CLI, console ou CI/CD.
- Sécurité et gestion des accès via IAM.

---

## 🧰 Composants Principaux

### 1. **Fonctions**
- Unité de déploiement : code + dépendances + configuration.
- Support de plusieurs runtimes (Node.js, Python, Go, Java…).

### 2. **Déclencheurs (Triggers)**
- HTTP : endpoints REST.
- Pub/Sub : messages sur un topic.
- Cloud Storage : ajout/modification de fichiers.
- Firestore, Firebase, etc.

### 3. **Variables d’environnement**
- Configuration dynamique des fonctions.

### 4. **IAM & Sécurité**
- Contrôle d’accès fin, gestion des permissions.

### 5. **Logs & Monitoring**
- Intégration avec Cloud Logging et Cloud Monitoring.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| API REST stateless                  | Création rapide d’APIs HTTP |
| Traitement d’événements             | Réaction à des uploads, messages Pub/Sub, etc. |
| Automatisation                      | Tâches planifiées ou automatisées |
| Intégration microservices           | Glue logic entre services GCP |
| Traitement de fichiers              | Transformation à la volée lors d’un upload |

---

## 🧑‍🔬 Exemple d’Architecture : Cloud Functions sur GCP

1. **Source d’événement** : [Pub/Sub](../PubSub/pubsub.md), [Cloud Storage](../Storage/storage.md), HTTP, etc.
2. **Fonction** : Déclenchée par l’événement, exécute le code.
3. **Traitement** : Logique métier, transformation, appel à d’autres APIs.
4. **Sortie** : Résultat stocké, envoyé ou déclenchement d’autres services.
5. **Monitoring** : Supervision via [Cloud Monitoring](../CloudMonitoring/cloudmonitoring.md) et [Cloud Logging](../CloudLogging/cloudlogging.md).

---

# 🚀 Commandes / Code utiles

### Exemple : Déployer une fonction HTTP en Python

```bash
gcloud functions deploy hello_http \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated \
  --region=europe-west1
```

## ✅ Bonnes Pratiques

- Gérer les secrets via Secret Manager ou variables d’environnement.
- Limiter les permissions IAM au strict nécessaire.
- Superviser les logs et métriques pour détecter les erreurs rapidement.
- Structurer le code pour faciliter la maintenance et les tests.
- Utiliser des fonctions courtes et spécialisées (Single Responsibility Principle).
- Automatiser les déploiements avec CI/CD.