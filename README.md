# 🍴 Analyse Exploratoire : Le Paysage de la Restauration à Bengaluru (Zomato)

**Cours :** 8PRO408 - Outils de programmation pour la science des données  
**Étudiant :** Pier-Luc Larouche  
**Date limite :** 19 décembre 2025 à 23h59

## 📌 Présentation du Projet
Ce projet consiste en une analyse exploratoire (EDA) approfondie du jeu de données Zomato, regroupant les informations de plus de 51 000 restaurants à Bengaluru, en Inde. L'objectif est de comprendre les dynamiques de marché, la répartition géographique des services et les facteurs influençant la popularité des établissements.

---

## 🎯 Objectifs de l'Analyse
Conformément aux exigences du projet, ce travail couvre :
1. **Nettoyage de données** : Traitement des formats de prix (coûts pour deux) et normalisation des notations (`rate`).
2. **Analyse Géographique** : Identification des zones à forte densité de restaurants et des quartiers spécialisés.
3. **Analyse de Segmentation** : Étude par type de service (Delivery, Dine-out, Pubs) et types de cuisines.
4. **Étude de Popularité** : Analyse de la relation entre le nombre de votes, le prix moyen et la note finale.
5. **Visualisation Interactive** : Création d'un dashboard interactif pour explorer les données par quartier.

---

## 📁 Organisation du Dépôt
L'organisation des fichiers suit les meilleures pratiques de la science des données pour assurer la reproductibilité :

```text
.
├── data/
│   └── zomato.csv          # Dataset
├── notebooks/
│   └── EDA_Zomato.ipynb    # Notebook Jupyter contenant l'analyse complète
├── app/
│   └── streamlit_app.py    # Code source de l'application interactive
├── reports/
│   └── Rapport_Final.pdf   # Rapport de synthèse (1-2 pages)
├── requirements.txt        # Liste des dépendances Python
└── README.md               # Documentation du projet (ce fichier)
```

---

## 🛠️ Installation et Utilisation

### 1. Installation des dépendances
Ouvrez votre terminal dans le dossier racine du projet et exécutez la commande suivante :
```bash
pip install -r requirements.txt
```

### 2. Lancement du Dashboard Streamlit
Pour explorer les données de manière interactive et visualiser les graphiques dynamiques :
```bash
streamlit run app/streamlit_app.py
```
---

## 📊 Synthèse des Observations
- **Densité et Localisation** : Les quartiers de BTM, HSR et Koramangala concentrent le plus grand nombre de restaurants, principalement axés sur la livraison (Delivery).

- **Profils de Prix** : Les quartiers centraux comme Lavelle Road et Residency Road affichent les coûts moyens les plus élevés, mais aussi les notations les plus constantes.

- **Corrélation Prix/Note** : Il existe une corrélation positive modérée : les établissements avec un investissement plus élevé (décor, service à table) obtiennent souvent de meilleures notes.

---

## 📝 Livrables
- [x] Notebook Jupyter documenté.

- [x] Rapport PDF de synthèse.

- [x] Application Streamlit fonctionnelle.

- [x] Dépôt GitHub organisé.