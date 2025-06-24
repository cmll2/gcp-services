# Data Studio

**Keywords**: `BI`, `Data Visualization`, `Reporting`, `Dashboards`, `GCP`, `Managed Services`, `Connectors`, `Analytics`

---

## 🧠 Description Générale

**Data Studio** (devenu Looker Studio) est un outil de Business Intelligence (BI) et de visualisation de données proposé par Google Cloud. Il permet de créer des tableaux de bord interactifs et des rapports personnalisés à partir de multiples sources de données.

Caractéristiques principales :
- Création de dashboards interactifs et partagés.
- Connexion à de nombreuses sources de données (BigQuery, Google Sheets, SQL, etc.).
- Visualisations variées : graphiques, tableaux, cartes, jauges, etc.
- Contrôle d’accès et partage granulaire.
- Calculs personnalisés, filtres et paramètres dynamiques.

---

## 🧰 Composants Principaux

### 1. **Sources de données**
- Connexion native à BigQuery, Google Sheets, Cloud SQL, CSV, etc.
- Connecteurs partenaires pour d’autres bases et APIs.

### 2. **Rapports**
- Création de rapports multi-pages avec visualisations interactives.
- Personnalisation avancée du design.

### 3. **Dashboards**
- Tableaux de bord dynamiques pour le suivi des KPIs et analyses.

### 4. **Contrôle d’accès**
- Partage des rapports avec des utilisateurs ou groupes.
- Gestion des droits en lecture ou édition.

### 5. **Calculs et filtres**
- Champs calculés, filtres, paramètres pour analyses avancées.

---

## 🧑‍💼 Cas d’Usage

| Cas d’usage                         | Description |
|------------------------------------|-------------|
| Reporting exécutif                  | Tableaux de bord pour la direction et les managers |
| Analyse marketing                   | Suivi des campagnes, trafic, conversions |
| Suivi opérationnel                  | Monitoring des opérations en temps réel |
| Self-service BI                     | Exploration autonome des données par les métiers |
| Partage de KPIs                     | Diffusion de KPIs à l’ensemble de l’organisation |

---

## 🧑‍🔬 Exemple d’Architecture : Data Studio sur GCP

1. **Sources** : [BigQuery](../BigQuery/bigquery.md), [Google Sheets](https://sheets.google.com), [Cloud SQL](../SQL/sql.md), etc.
2. **Connexion** : Ajout des sources dans Data Studio via connecteurs natifs.
3. **Rapports** : Création de rapports et dashboards personnalisés.
4. **Partage** : Diffusion des rapports via liens, email ou intégration web.

---

# 🚀 Commandes / Code utiles

> Data Studio est principalement utilisé via l’interface web, il n’y a pas de commandes CLI ou API pour la création de rapports, mais vous pouvez automatiser la préparation des données avec BigQuery, Cloud SQL, etc.

---

## ✅ Bonnes Pratiques

- Centraliser les sources de données pour garantir la cohérence des analyses.
- Utiliser des filtres et paramètres pour des dashboards dynamiques.
- Contrôler finement les accès aux rapports selon la sensibilité des données.
- Documenter les rapports pour faciliter leur prise en main.
- Mettre à jour régulièrement les sources et les visualisations pour garder les analyses pertinentes.

---