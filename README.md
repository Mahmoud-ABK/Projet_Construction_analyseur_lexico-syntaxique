# 🛒 Système de Recommandation de Produits

Ce projet met en œuvre un système intelligent de recommandation de produits, visant à **adapter les suggestions aux préférences des utilisateurs** en analysant à la fois les **caractéristiques des produits** et les **sentiments exprimés** par les utilisateurs dans leurs retours.

Le système repose sur l’intégration de **techniques de traitement du langage naturel** (NLP), de **machine learning** et d’un **frontend interactif** pour offrir une expérience utilisateur moderne et dynamique.

---

## 🚀 Objectif du projet

- Offrir des **recommandations de produits personnalisées** basées sur l’analyse sémantique des avis clients.
- Exploiter les **données textuelles** pour extraire des insights pertinents.
- Proposer une interface web interactive pour la consultation des résultats.

---

## 🔍 Fonctionnalités principales

### 🧩 Analyse Lexicale

- **Objectif** : Découper les textes en unités de base (« tokens »)
- **Techniques** :
  - Expressions régulières (`re`) pour identifier mots-clés, chiffres, symboles
  - Utilisation de **SpaCy** pour détecter les types de mots (nom, verbe, adjectif, etc.) et améliorer l’extraction d’informations contextuelles

### 🧠 Analyse Syntaxique

- **Objectif** : Valider la structure grammaticale des textes
- **Méthode** :
  - Construction d’un **arbre syntaxique** pour représenter les relations hiérarchiques entre les éléments du texte

### 💬 Analyseur de Sentiments

- **Objectif** : Comprendre les émotions exprimées dans les avis
- **Techniques** :
  - Modèles de **machine learning** pour détecter des sentiments dominants : positifs, négatifs, ou neutres
  - Recommandations dynamiques selon les émotions détectées
    - Ex : Avis positifs → mise en avant des atouts du produit

---

## 💻 Technologies utilisées

- **Python**
  - Bibliothèques : `re`, `spacy`
- **Framework Web** : Flask
- **Frontend** : HTML / CSS / JavaScript
- **Interface Web** :
  - Affichage moderne et interactif des analyses et recommandations

---

## 👥 Auteurs

- **Rayen Braiek**
- **Fares Aloulou**
- **Ranim Bouraoui**
- **Mariem Boughizene**
- **Mahmoud Ben Abdelkader**
