# Kubeflow Pipelines

**Keywords**: `ML Pipelines`, `Orchestration`, `Kubeflow`, `MLOps`, `Workflow`, `Kubernetes`, `Automation`, `GCP`, `Open Source`

---

## 🧠 Description Générale

**Kubeflow Pipelines** est un composant de la plateforme Kubeflow permettant de concevoir, exécuter et gérer des workflows de Machine Learning (ML) reproductibles et automatisés sur Kubernetes. Il facilite l’orchestration des étapes du cycle de vie ML (prétraitement, entraînement, validation, déploiement).

Caractéristiques principales :
- Définition de pipelines ML sous forme de code (Python).
- Orchestration d’étapes (components) conteneurisées.
- Suivi des exécutions, des métriques et des artefacts.
- Versioning des pipelines et des exécutions.
- Intégration avec Vertex AI, GKE, MinIO, S3, etc.
- UI web pour visualiser, lancer et monitorer les pipelines.

---

## 🧰 Composants Principaux

### 1. **Pipeline**
- Workflow ML composé de plusieurs étapes (components).
- Décrit en Python via le SDK Kubeflow Pipelines.

### 2. **Component**
- Étape individuelle du pipeline, packagée en conteneur Docker.
- Réutilisable et paramétrable.

### 3. **Experiment**
- Groupe d’exécutions de pipelines pour comparer les résultats.

### 4. **Run**
- Exécution d’un pipeline avec des paramètres spécifiques.

### 5. **Artifact Store**
- Stockage des artefacts produits (modèles, métriques, logs).

### 6. **UI & API**
- Interface web et API REST pour gérer les pipelines.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Orchestration ML                    | Automatisation du cycle de vie ML (data prep, train, deploy) |
| MLOps                               | CI/CD pour modèles ML sur Kubernetes |
| Reproductibilité scientifique       | Versioning des pipelines et des artefacts |
| Hyperparameter tuning               | Lancer des expériences avec différents paramètres |
| Monitoring et audit                 | Suivi des exécutions, logs, métriques |

---

## 🧑‍🔬 Exemple d’Architecture : Kubeflow Pipelines sur GCP

1. **Stockage** : Données sur [Cloud Storage](../Storage/storage.md) ou S3.
2. **Cluster Kubernetes** : [GKE](../KubernetesEngine/kubernetesengine.md) hébergeant Kubeflow.
3. **Pipeline** : Décrit en Python, déployé via le SDK ou l’UI.
4. **Exécution** : Orchestration des étapes dans des pods Kubernetes.
5. **Monitoring** : Suivi via l’UI Kubeflow, [Cloud Monitoring](../CloudMonitoring/cloudmonitoring.md), [Cloud Logging](../CloudLogging/cloudlogging.md).

---

# 🚀 Commandes / Code utiles

### Exemple : Définir un pipeline simple en Python

```python
import kfp
from kfp import dsl

@dsl.pipeline(
    name='Exemple pipeline',
    description='Un pipeline Kubeflow simple'
)
def my_pipeline(param1: str):
    op1 = dsl.ContainerOp(
        name='Step 1',
        image='python:3.9',
        command=['python', '-c'],
        arguments=['print("Hello, Kubeflow!")']
    )

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(my_pipeline, 'pipeline.yaml')
```

## ✅ Bonnes Pratiques

- Versionner les pipelines et les artefacts pour la traçabilité.
- Utiliser des images Docker légères et reproductibles pour les components.
- Sécuriser l’accès au cluster et aux données (IAM, RBAC).
- Automatiser les tests et le déploiement des pipelines (CI/CD).
- Surveiller les exécutions et logs pour détecter les erreurs rapidement.
- Documenter chaque étape et paramètre du pipeline.