# Looker

**Keywords**: `BI`, `Data Visualization`, `Analytics`, `Reporting`, `Dashboards`, `Exploration`, `GCP`, `Managed Services`

---

## 🧠 Description Générale

**Looker** est une plateforme de Business Intelligence (BI) et d’analytique moderne proposée par Google Cloud. Elle permet d’explorer, d’analyser et de visualiser les données issues de différentes sources, tout en centralisant la gouvernance et la modélisation des données.

Caractéristiques principales :
- Création de tableaux de bord interactifs et de rapports personnalisés.
- Exploration ad hoc des données via une interface intuitive.
- Modélisation des données avec LookML (langage de modélisation propriétaire).
- Intégration avec de nombreuses sources de données (BigQuery, Cloud SQL, Snowflake, etc.).
- Partage et collaboration sur les analyses et dashboards.
- Sécurité et gouvernance centralisées.

---

## 🧰 Composants Principaux

### 1. **Dashboards**
- Visualisation interactive des données sous forme de graphiques, tableaux, cartes, etc.
- Rafraîchissement automatique des données.

### 2. **Explorations**
- Analyse ad hoc des données par glisser-déposer.
- Possibilité de sauvegarder et partager les explorations.

### 3. **LookML**
- Langage de modélisation pour définir les dimensions, mesures, relations et autorisations.
- Centralisation de la logique métier.

### 4. **Alertes et planifications**
- Déclenchement d’alertes sur seuils ou conditions.
- Planification d’envoi automatique de rapports.

### 5. **Intégrations**
- Connexion à de multiples bases de données cloud ou on-premise.
- API pour automatiser les workflows BI.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Tableaux de bord exécutifs          | Suivi des KPIs et reporting pour la direction |
| Analyse commerciale                 | Exploration des ventes, marges, clients |
| Monitoring opérationnel             | Suivi en temps réel des opérations |
| Self-service BI                     | Exploration autonome des données par les métiers |
| Gouvernance des données             | Centralisation des règles et de la sécurité |

---

## 🧑‍🔬 Exemple d’Architecture : Looker sur GCP

1. **Sources de données** : [BigQuery](../BigQuery/bigquery.md), [Cloud SQL](../SQL/sql.md), autres bases compatibles SQL.
2. **Modélisation** : Définition des modèles de données avec LookML.
3. **Visualisation** : Création de dashboards et rapports dans Looker.
4. **Partage** : Diffusion des analyses via liens, exports, alertes ou API.

---

# 🚀 Commandes / Code utiles

### Exemple : Connexion Looker à BigQuery

- Depuis l’interface Looker, ajouter une connexion :
  - Type : BigQuery
  - Project ID : `your-gcp-project`
  - Dataset : `your_dataset`
  - Authentification via service account JSON

### Exemple : Modèle LookML simple

```lookml
view: orders {
  sql_table_name: your_dataset.orders ;;

  dimension: order_id {
    primary_key: yes
    type: string
    sql: ${TABLE}.order_id ;;
  }

  measure: total_amount {
    type: sum
    sql: ${TABLE}.amount ;;
  }
}
```

## ✅ Bonnes Pratiques

- Centraliser la logique métier dans LookML pour garantir la cohérence des analyses.
- Utiliser les permissions et groupes pour sécuriser l’accès aux données sensibles.
- Documenter les modèles et dashboards pour faciliter la prise en main.
- Planifier des rafraîchissements et alertes pour un suivi proactif.
- Favoriser le self-service BI tout en gardant la gouvernance centralisée.