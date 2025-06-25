# Kubeflow

**Keywords**: `MLOps`, `Kubernetes`, `Machine Learning`, `Pipelines`, `Open Source`, `Automation`, `Workflow`, `GCP`, `Model Training`, `Serving`

---

## 🧠 Description Générale

**Kubeflow** est une plateforme open source pour l’orchestration, l’automatisation et la gestion du cycle de vie du Machine Learning sur Kubernetes. Elle vise à rendre le déploiement de workflows ML reproductible, portable et scalable.

Caractéristiques principales :
- Déploiement de pipelines ML sur Kubernetes.
- Gestion des notebooks Jupyter pour le prototypage.
- Orchestration des étapes ML (prétraitement, entraînement, validation, déploiement).
- Serving de modèles (KFServing, Seldon Core).
- Gestion des utilisateurs, sécurité et accès via IAM/RBAC.
- Intégration avec des outils de monitoring et de logging.

---

## 🧰 Composants Principaux

### 1. **Notebooks**
- Environnements Jupyter gérés pour le développement et l’exploration.

### 2. **Pipelines**
- Orchestration de workflows ML reproductibles (voir [Kubeflow Pipelines](../Kubeflow/pipelines.md)).

### 3. **Training Operators**
- Support de l’entraînement distribué (TFJob, PyTorchJob, MXJob…).

### 4. **Serving**
- Déploiement et gestion de modèles en production (KFServing, Seldon Core).

### 5. **Katib**
- Optimisation automatique des hyperparamètres (AutoML).

### 6. **Central Dashboard**
- Interface web pour gérer tous les composants Kubeflow.

### 7. **Multi-user & Sécurité**
- Gestion des espaces de travail, accès et isolation via namespaces et RBAC.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| MLOps complet                       | Automatisation du cycle de vie ML sur Kubernetes |
| Entraînement distribué              | Utilisation de GPU/TPU pour le deep learning |
| Pipelines reproductibles            | Orchestration et versioning des workflows ML |
| Déploiement de modèles              | Serving scalable et sécurisé sur Kubernetes |
| Optimisation AutoML                 | Recherche automatique des meilleurs hyperparamètres |

---

## 🧑‍🔬 Exemple d’Architecture : Kubeflow sur GCP

1. **Cluster Kubernetes** : [GKE](../KubernetesEngine/kubernetesengine.md) hébergeant Kubeflow.
2. **Stockage** : [Cloud Storage](../Storage/storage.md) pour les datasets et artefacts.
3. **Notebooks** : Prototypage et exploration des données.
4. **Pipelines** : Orchestration des workflows ML.
5. **Serving** : Déploiement des modèles via KFServing/Seldon.
6. **Monitoring** : Supervision via [Cloud Monitoring](../CloudMonitoring/cloudmonitoring.md) et [Cloud Logging](../CloudLogging/cloudlogging.md).

---

# 🚀 Commandes / Code utiles

### Exemple : Déployer Kubeflow sur GKE (via kfctl)

```bash
kfctl apply -V -f https://raw.githubusercontent.com/kubeflow/manifests/master/kfdef/kfctl_gcp_iap.yaml
```

## ✅ Bonnes Pratiques

- Séparer les environnements (dev, staging, prod) par namespace Kubernetes.
- Gérer les accès avec IAM et RBAC pour la sécurité.
- Versionner les pipelines, modèles et datasets.
- Automatiser le déploiement avec des scripts ou des outils IaC (Terraform, kustomize).
- Surveiller les ressources et les logs pour détecter rapidement les problèmes.
- Documenter chaque étape du workflow ML pour la reproductibilité.