# Compute Engine

**Keywords**: `VM`, `IaaS`, `Virtual Machines`, `Scalable`, `Custom Images`, `GPU`, `GCP`, `Managed Services`, `Autoscaling`, `Networking`

---

## 🧠 Description Générale

**Compute Engine** est le service d’Infrastructure as a Service (IaaS) de Google Cloud permettant de créer et gérer des machines virtuelles (VM) hautement configurables. Il offre des options de personnalisation avancées pour le CPU, la mémoire, le stockage, le réseau et les accélérateurs (GPU/TPU).

Caractéristiques principales :
- Création de VM à la demande ou via des templates.
- Choix de systèmes d’exploitation (Linux, Windows, etc.).
- Support des disques persistants, SSD, local SSD.
- Intégration avec les réseaux VPC, load balancers, firewalls.
- Possibilité d’utiliser des images personnalisées ou des snapshots.
- Autoscaling et groupes d’instances managés.
- Accélérateurs matériels (GPU, TPU).

---

## 🧰 Composants Principaux

### 1. **Instances**
- Machines virtuelles individuelles, configurables à la création.

### 2. **Groupes d’instances**
- Gestion de clusters de VM pour le scaling automatique et la haute disponibilité.

### 3. **Disques**
- Disques persistants, SSD, local SSD, snapshots pour la sauvegarde/restauration.

### 4. **Images**
- Images publiques, privées ou personnalisées pour déployer rapidement des VM.

### 5. **Réseau & Sécurité**
- Intégration avec VPC, sous-réseaux, firewalls, adresses IP publiques/privées.

### 6. **Accélérateurs**
- Ajout de GPU ou TPU pour les workloads intensifs (ML, calcul scientifique).

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Hébergement d’applications          | Déploiement d’applications web, API, backend |
| Calcul intensif                     | Workloads ML, rendu 3D, simulations |
| Environnements de développement     | VM pour dev/test personnalisés |
| Migration de serveurs               | Reprise d’infrastructure on-premise |
| Groupes d’instances managés         | Scalabilité automatique pour frontends ou batchs |

---

## 🧑‍🔬 Exemple d’Architecture : Compute Engine sur GCP

1. **Déploiement** : Création d’instances via la console, gcloud ou Terraform.
2. **Stockage** : Disques persistants, snapshots pour la sauvegarde.
3. **Réseau** : Intégration avec VPC, load balancers, firewalls.
4. **Monitoring** : Supervision via [Cloud Monitoring](../CloudMonitoring/cloudmonitoring.md) et [Cloud Logging](../CloudLogging/cloudlogging.md).
5. **Autoscaling** : Groupes d’instances managés pour le scaling automatique.

---

# 🚀 Commandes / Code utiles

### Exemple : Créer une VM

```bash
gcloud compute instances create my-vm \
  --zone=europe-west1-b \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud
```

### Exemple : ajouter un GPU à une VM

```bash
gcloud compute instances create my-gpu-vm \
  --zone=europe-west1-b \
  --machine-type=n1-standard-4 \
  --accelerator=type=nvidia-tesla-k80,count=1 \
  --image-family=common-cu110 \
  --image-project=ml-images
```

## ✅ Bonnes Pratiques

- Utiliser des groupes d’instances managés pour le scaling et la haute disponibilité.
- Planifier des snapshots réguliers pour la sauvegarde des données.
- Sécuriser les accès SSH avec des clés et IAM.
- Optimiser les coûts en arrêtant les VM inutilisées.
- Superviser les performances avec Cloud Monitoring et Logging.
- Utiliser des images personnalisées pour standardiser les déploiements.