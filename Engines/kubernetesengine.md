# Kubernetes Engine

**Keywords**: `Kubernetes`, `Containers`, `Orchestration`, `GKE`, `Scaling`, `Managed`, `DevOps`, `GCP`, `CI/CD`

---

## 🧠 Description Générale

**Google Kubernetes Engine (GKE)** est un service managé de Google Cloud pour déployer, gérer et scaler des applications conteneurisées avec Kubernetes. Il simplifie l’orchestration, la sécurité, la mise à l’échelle et la maintenance des clusters Kubernetes.

Caractéristiques principales :
- Provisionnement automatique de clusters Kubernetes.
- Mise à l’échelle automatique des nœuds et des pods.
- Mises à jour automatiques et gestion simplifiée des versions.
- Sécurité avancée (IAM, RBAC, VPC, secrets).
- Intégration avec les outils CI/CD, monitoring et logging GCP.

---

## 🧰 Composants Principaux

### 1. **Clusters**
- Ensemble de machines virtuelles (nœuds) gérées par Kubernetes.
- Clusters zonaux, régionaux ou autopilotés.

### 2. **Nodes (Nœuds)**
- Machines virtuelles qui exécutent les pods.
- Gestion automatique du cycle de vie.

### 3. **Pods**
- Plus petite unité déployable, contenant un ou plusieurs conteneurs.

### 4. **Services**
- Exposent les applications (LoadBalancer, NodePort, ClusterIP).

### 5. **Ingress**
- Gestion avancée du routage HTTP(S) et SSL.

### 6. **Workloads**
- Déploiements, StatefulSets, DaemonSets, Jobs, CronJobs.

### 7. **IAM & Sécurité**
- Contrôle d’accès via IAM, RBAC, secrets, Workload Identity.

### 8. **Monitoring & Logging**
- Intégration avec Cloud Monitoring et Cloud Logging.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Microservices                       | Déploiement et gestion d’architectures microservices |
| CI/CD                               | Automatisation des déploiements avec pipelines |
| Traitement batch                    | Exécution de jobs ponctuels ou planifiés |
| Applications web scalables          | Mise à l’échelle automatique selon la charge |
| Machine Learning                    | Déploiement de modèles ML dans des conteneurs |

---

## 🧑‍🔬 Exemple d’Architecture : GKE sur GCP

1. **Source code** : Stocké sur [Cloud Source Repositories](../CloudSourceRepositories/cloudsourcerepositories.md) ou GitHub.
2. **CI/CD** : Pipelines avec [Cloud Build](../CloudBuild/cloudbuild.md) ou Jenkins.
3. **Container Registry** : Images stockées sur [Artifact Registry](../ArtifactRegistry/artifactregistry.md).
4. **Cluster GKE** : Déploiement des workloads.
5. **Monitoring** : [Cloud Monitoring](../CloudMonitoring/cloudmonitoring.md), [Cloud Logging](../CloudLogging/cloudlogging.md).
6. **Load Balancer** : Exposition des services via Ingress.

---

# 🚀 Commandes / Code utiles

### Exemple : Création d’un cluster GKE

```bash
gcloud container clusters create my-cluster \
  --zone europe-west1-b \
  --num-nodes 3
```

### Exemple : Déploiement d'une application

```bash
kubectl create deployment hello-app --image=gcr.io/google-samples/hello-app:1.0
kubectl expose deployment hello-app --type=LoadBalancer --port 80 --target-port 8080
```

### Exemple : Mise à l'échelle automatique

```bash
kubectl autoscale deployment hello-app --cpu-percent=50 --min=1 --max=10
```

## ✅ Bonnes Pratiques

- Utiliser Workload Identity pour sécuriser l’accès aux ressources GCP.
- Activer l’autoscaling pour optimiser les coûts et la performance.
- Séparer les environnements (dev, staging, prod) par namespace.
- Superviser les clusters avec Cloud Monitoring et Cloud Logging.
- Automatiser les déploiements avec des pipelines CI/CD.
- Mettre à jour régulièrement les versions de Kubernetes et des nœuds.
