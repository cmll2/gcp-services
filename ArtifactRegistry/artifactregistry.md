# Artifact Registry

**Keywords**: `Container Registry`, `Artifacts`, `Docker`, `Maven`, `npm`, `Python`, `CI/CD`, `GCP`, `Managed Services`, `Security`

---

## 🧠 Description Générale

**Artifact Registry** est le service de gestion d’artefacts de Google Cloud. Il permet de stocker, gérer et sécuriser des images de conteneurs (Docker), des paquets (Maven, npm, Python, etc.) et d’autres artefacts utilisés dans les pipelines CI/CD.

Caractéristiques principales :
- Support des images Docker, paquets Maven, npm, Python, et plus.
- Contrôle d’accès fin via IAM.
- Intégration native avec GKE, Cloud Build, Cloud Run, etc.
- Scanning de vulnérabilités intégré.
- Réplication multi-région et gestion du cycle de vie des artefacts.

---

## 🧰 Composants Principaux

### 1. **Dépôts (Repositories)**
- Espaces logiques pour stocker des artefacts (Docker, Maven, npm, etc.).
- Types : Docker, Maven, npm, Python, Apt, Yum.

### 2. **Artefacts**
- Images de conteneurs, paquets applicatifs, librairies, etc.

### 3. **Contrôle d’accès**
- Gestion des permissions via IAM.
- Intégration avec les identités de service.

### 4. **Sécurité**
- Scanning automatique des vulnérabilités.
- Gestion des versions et du cycle de vie.

### 5. **Intégration CI/CD**
- Utilisation directe dans les pipelines Cloud Build, GKE, Cloud Run, etc.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Stockage d’images Docker            | Registry sécurisé pour images de conteneurs |
| Dépôt de paquets applicatifs        | Maven, npm, Python pour la distribution interne |
| Sécurité des artefacts              | Scanning de vulnérabilités et gestion des accès |
| Automatisation CI/CD                | Intégration dans les pipelines de build et déploiement |
| Multi-cloud                         | Distribution d’artefacts sur plusieurs régions ou clouds |

---

## 🧑‍🔬 Exemple d’Architecture : Artifact Registry sur GCP

1. **Build** : Création d’images ou paquets avec [Cloud Build](../CloudBuild/cloudbuild.md).
2. **Stockage** : Dépôt dans Artifact Registry (Docker, Maven, npm, etc.).
3. **Déploiement** : Utilisation des artefacts dans [GKE](../KubernetesEngine/kubernetesengine.md), [Cloud Run](../CloudRun/cloudrun.md), etc.
4. **Sécurité** : Scanning automatique et gestion des accès.
5. **Monitoring** : Suivi des accès et des vulnérabilités via [Cloud Monitoring](../CloudMonitoring/cloudmonitoring.md).

---

# 🚀 Commandes / Code utiles

### Exemple : Créer un dépôt Docker

```bash
gcloud artifacts repositories create my-docker-repo \
  --repository-format=docker \
  --location=europe-west1 \
  --description="Dépôt Docker pour mon équipe"
```

### Exemple : Pousser une image docker

```bash
docker tag my-image europe-west1-docker.pkg.dev/your-project/my-docker-repo/my-image:tag
docker push europe-west1-docker.pkg.dev/your-project/my-docker-repo/my-image:tag
```

## ✅ Bonnes Pratiques

- Utiliser des dépôts séparés par environnement (dev, staging, prod).
- Activer le scanning de vulnérabilités pour tous les artefacts.
- Gérer les accès avec IAM et les identités de service.
- Nettoyer régulièrement les artefacts obsolètes avec des règles de cycle de vie.
- Intégrer Artifact Registry dans vos pipelines CI/CD pour automatiser la gestion des artefacts.