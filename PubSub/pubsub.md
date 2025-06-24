# Pub/Sub

**Keywords**: `Messaging`, `Event-Driven`, `Streaming`, `Asynchronous`, `GCP`, `Managed Services`, `Serverless`

---

## 🧠 Description Générale

**Pub/Sub** (Publish/Subscribe) est un service de messagerie entièrement géré et serverless proposé par Google Cloud. Il permet de créer des architectures événementielles et de diffuser des messages entre des systèmes de manière asynchrone.

Caractéristiques principales :
- Communication asynchrone entre producteurs et consommateurs.
- Évolutivité automatique pour gérer des millions de messages par seconde.
- Garantie de livraison au moins une fois.
- Intégration avec d'autres services GCP comme Dataflow, Cloud Functions, BigQuery.

---

## 🧰 Composants Principaux

### 1. **Topics**
- Point d'entrée pour les messages publiés par les producteurs.
- Chaque message est envoyé à un ou plusieurs abonnés via des abonnements.

### 2. **Subscriptions**
- Point de sortie pour les messages consommés par les abonnés.
- Deux types :
  - **Pull** : Les abonnés récupèrent les messages.
  - **Push** : Les messages sont envoyés automatiquement à un endpoint HTTP.

### 3. **Messages**
- Contiennent des données (payload) et des métadonnées (attributs).
- Taille maximale : 10 Mo.

### 4. **Dead Letter Topics (DLT)**
- Stockage des messages non livrés après plusieurs tentatives.

### 5. **Ordering Keys**
- Permettent de garantir l'ordre des messages pour un même producteur.

### 6. **Replay**
- Fonctionnalité permettant de rejouer des messages déjà consommés.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Traitement d'événements en temps réel | Diffusion d'événements à des systèmes de traitement comme Dataflow |
| Intégration de microservices        | Communication asynchrone entre microservices |
| Collecte de logs                    | Envoi de logs vers des systèmes d'analyse comme BigQuery |
| Notifications                       | Envoi de notifications push à des applications mobiles ou web |
| Streaming IoT                       | Transmission de données IoT vers des pipelines de traitement |

---

## 🧑‍🔬 Exemple d’Architecture : Pub/Sub avec Dataflow

1. **Source d'événements** : [IoT Core](../IoTCore/iotcore.md) ou application externe.
2. **Topic Pub/Sub** : Réception des messages.
3. **Pipeline de traitement** : [Dataflow](../Dataflow/dataflow.md) pour transformation et enrichissement.
4. **Stockage** : [BigQuery](../BigQuery/bigquery.md) ou [Cloud Storage](../CloudStorage/cloudstorage.md).
5. **Visualisation** : [Looker](../Looker/looker.md) ou [Data Studio](../DataStudio/datastudio.md).

---

# 🚀 Commandes / Code utiles

### Exemple : Publication d'un message

```python
from google.cloud import pubsub_v1

project_id = "your-project-id"
topic_id = "your-topic-id"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

data = "Hello, Pub/Sub!".encode("utf-8")
future = publisher.publish(topic_path, data, origin="python-sample", username="user123")
print(f"Message publié : {future.result()}")
```

### Exemple : Souscription à un topic

```python
from google.cloud import pubsub_v1

project_id = "your-project-id"
subscription_id = "your-subscription-id"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):
    print(f"Message reçu : {message.data}")
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Écoute des messages sur {subscription_path}...")

try:
    streaming_pull_future.result()
except KeyboardInterrupt:
    streaming_pull_future.cancel()
```

```python
from google.cloud import pubsub_v1
project_id = "your-project-id"
topic_id = "your-topic-id"
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)
topic = publisher.create_topic(name=topic_path)
print(f"Topic créé : {topic.name}")
```

### ✅ Bonnes Pratiques

- Utiliser des Dead Letter Topics pour gérer les messages non livrés.
- Configurer des timeouts pour éviter les blocages dans les abonnements.
- Activer les Ordering Keys si l'ordre des messages est critique.
- Superviser les métriques avec Cloud Monitoring.
- Utiliser des abonnements Push pour des systèmes réactifs.