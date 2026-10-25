# ReadClean

ReadClean est un petit outil Python pour extraire le contenu principal d'une page web et le convertir en un fichier Markdown propre, avec les métadonnées de l'article (titre, auteur, date et source).

Le projet utilise `trafilatura` pour récupérer et nettoyer le contenu, puis `markdownify` pour le convertir en Markdown. Le script permet aussi d'ajouter un front matter YAML, pratique pour les outils comme Obsidian, Notion ou d'autres gestionnaires de notes.

## Fonctionnalités

- Téléchargement d'une page web à partir de son URL
- Extraction du contenu principal sans le bruit de la page
- Récupération du titre, de l'auteur et de la date
- Conversion du HTML en Markdown
- Génération d'un fichier de sortie prêt à être utilisé dans un carnet de notes ou un système de documentation

## Prérequis

- Python 3.9+
- pip

## Installation

1. Cloner le projet :

```bash
git clone <url-du-projet>
cd readclean
```

2. Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python main.py "https://example.com/article" -o article.md
```

### Paramètres

- `url` : URL de la page web à traiter
- `-o, --output` : nom du fichier Markdown de sortie (par défaut : `article.md`)

## Exemple de sortie

Le script génère un fichier Markdown de ce type :

```md
---
title: "Titre de l'article"
author: "Auteur"
date: "2026-10-08"
source: "https://example.com/article"
---

# Titre principal

Contenu de l'article extrait et converti en Markdown.
```

## Structure du projet

```text
readclean/
├── main.py
├── scraper.py
├── requirements.txt
├── article.md
└── README.md
```

- `main.py` : point d'entrée CLI
- `scraper.py` : logique d'extraction et conversion du contenu
- `requirements.txt` : dépendances Python
- `article.md` : exemple de fichier de sortie généré

## Dépendances

- `trafilatura`
- `markdownify`
- `rich`

## Exemple de commande complète

```bash
python main.py "https://www.lemonde.fr/" -o mon_article.md
```

Le programme enregistrera le résultat dans `mon_article.md`.

## Licence

Ce projet est fourni sans licence spécifique dans le dépôt actuel. Si vous souhaitez le distribuer ou l'utiliser en production, ajoutez une licence adaptée selon votre usage.
