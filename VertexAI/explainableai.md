# Explainable AI

**Keywords**: `Explainability`, `Interpretability`, `Machine Learning`, `SHAP`, `Integrated Gradients`, `Model Transparency`, `GCP`, `Responsible AI`

---

## 🧠 Description Générale

**Explainable AI** est un ensemble d'outils et de techniques proposés par Google Cloud pour rendre les modèles de Machine Learning plus transparents et interprétables. Il aide les utilisateurs à comprendre comment et pourquoi un modèle prend des décisions, ce qui est essentiel pour des domaines sensibles comme la finance, la santé ou les assurances.

Caractéristiques principales :
- Explications locales et globales des prédictions.
- Supporte les modèles AutoML et les modèles personnalisés.
- Méthodes d'explicabilité comme **SHAP**, **Integrated Gradients**, et **XRAI**.
- Intégration avec Vertex AI pour superviser les modèles en production.

---

## 🧰 Composants Principaux

### 1. **Explications Locales**
- Fournissent des informations sur les caractéristiques qui influencent une prédiction spécifique.
- Exemple : Pourquoi un prêt a été approuvé ou refusé.

### 2. **Explications Globales**
- Fournissent une vue d'ensemble des caractéristiques les plus importantes pour le modèle.
- Exemple : Identifier les variables les plus influentes dans un modèle de prédiction de churn.

### 3. **Méthodes d'Explicabilité**
- **SHAP (SHapley Additive exPlanations)** : Attribution de l'importance des caractéristiques en utilisant la théorie des jeux.
- **Integrated Gradients** : Analyse des gradients pour mesurer l'impact des caractéristiques.
- **XRAI (eXplainable Region-based AI)** : Explicabilité basée sur les régions pour les modèles de vision.

### 4. **Intégration avec Vertex AI**
- Génération d'explications pour les modèles déployés sur Vertex AI.
- Monitoring des dérives des caractéristiques pour détecter les biais en production.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Finance                             | Comprendre pourquoi un prêt ou une assurance a été approuvé/refusé |
| Santé                               | Identifier les facteurs influençant un diagnostic ou une prédiction médicale |
| Marketing                           | Analyser les variables influençant la prédiction de churn ou de conversion |
| Détection de fraude                 | Comprendre les décisions des modèles de détection d'anomalies |
| Vision par ordinateur               | Identifier les régions d'une image qui influencent une prédiction |

---

## 🧑‍🔬 Exemple d’Architecture : Explainable AI avec Vertex AI

1. **Source de données** : Données tabulaires, images ou texte.
2. **Modèle** : Entraînement d'un modèle avec AutoML ou un modèle personnalisé.
3. **Explicabilité** : Génération d'explications locales et globales avec Explainable AI.
4. **Déploiement** : Déploiement du modèle sur Vertex AI.
5. **Monitoring** : Supervision des dérives des caractéristiques et des performances du modèle.

---

# 🚀 Commandes / Code utiles

### Exemple : Générer des explications pour un modèle déployé

```python
from google.cloud import aiplatform

aiplatform.init(project="your-project-id", location="us-central1")

endpoint = aiplatform.Endpoint(endpoint_name="projects/your-project-id/locations/us-central1/endpoints/your-endpoint-id")

instances = [
    {"feature1": 5.1, "feature2": 3.5, "feature3": 1.4, "feature4": 0.2}
]

response = endpoint.explain(instances=instances)
for explanation in response.explanations:
    print("Explications locales :")
    for attribution in explanation.attributions:
        print(f"Caractéristique : {attribution.feature_name}, Importance : {attribution.attribution_score}")
```

### Exemple : Activer Explainable AI lors du déploiement d'un modèle

```python
from google.cloud import aiplatform

aiplatform.init(project="your-project-id", location="us-central1")

model = aiplatform.Model(model_name="projects/your-project-id/locations/us-central1/models/your-model-id")

endpoint = model.deploy(
    deployed_model_display_name="explainable-model",
    machine_type="n1-standard-4",
    explanation_metadata={
        "inputs": {
            "feature1": {"input_tensor_name": "feature1", "encoding": "BAG_OF_FEATURES"},
            "feature2": {"input_tensor_name": "feature2", "encoding": "IDENTITY"},
        },
        "outputs": {"output_tensor_name": "predicted_value"},
    },
    explanation_parameters={
        "sampled_shapley_attribution": {"path_count": 10}
    },
)
print(f"Modèle déployé avec explicabilité activée : {endpoint.resource_name}")
```

## ✅ Bonnes Pratiques

- Utiliser des explications locales pour analyser des prédictions spécifiques.
- Superviser les dérives des caractéristiques pour détecter les biais en production.
- Activer Explainable AI dès le déploiement pour les cas sensibles (finance, santé).
- Tester différentes méthodes d'explicabilité (SHAP, Integrated Gradients) pour - choisir la plus adaptée.
- Documenter les résultats des explications pour améliorer la transparence auprès des parties prenantes.