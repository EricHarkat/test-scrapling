# Test Scrapling

Découverte de la bibliothèque [Scrapling](https://github.com/D4Vinci/Scrapling) — un scraper Python qui retrouve les éléments d'une page même si le HTML a changé.

## Ce que fait ce projet

- Scrape les 100 citations de [quotes.toscrape.com](https://quotes.toscrape.com) (10 pages)
- Extrait le texte, l'auteur et les tags de chaque citation
- Sauvegarde le résultat dans `citations.json`
- Démontre le tracking d'éléments avec `save()` / `relocate()`

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Utilisation

```bash
python scraper.py
```

Le fichier `citations.json` est généré à la racine du projet.

## Features Scrapling explorées

### Scraping classique
`Fetcher` télécharge la page, `.css()` sélectionne les éléments par sélecteur CSS, `.text` lit le contenu.

### Pagination automatique
On suit le bouton "Next" avec `.css(".next a")` et `.urljoin()` jusqu'à ce qu'il disparaisse.

### Tracking d'éléments (`adaptive=True`)
La feature la plus unique de Scrapling : `save()` mémorise l'empreinte d'un élément (tag, attributs, texte, parent, voisins), et `relocate()` le retrouve sur une version modifiée de la page même si son sélecteur CSS est cassé.

```python
# Sauvegarder l'empreinte
page_v1.save(element, "mon_element")

# Retrouver sur une page restructurée
empreinte = page_v1.retrieve("mon_element")
retrouve = page_v2.relocate(empreinte, selector_type=True)
```
