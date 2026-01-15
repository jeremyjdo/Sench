# Sench - Instructions Claude Code

## Projet

**Sench** est un sub-agent de competitive intelligence pour **Claude Code**, **Codex** et **Cursor**. Il scrape des sites web d'entreprises et retourne le contenu + prompts d'analyse pour que l'IA hôte effectue l'analyse.

## Architecture

Sench est un **sub-agent** (pas un CLI standalone) :
1. Scrape le site web avec Playwright
2. Extrait le contenu, les liens sociaux, prend un screenshot
3. Retourne le contenu + prompts formatés
4. L'IA hôte (Claude Code/Codex/Cursor) analyse le contenu

**Pas de clé API requise** - l'analyse est faite par l'assistant de code.

## Stack Technique

| Layer | Tech |
|-------|------|
| CLI | argparse |
| Scraping | Playwright |

## Structure du projet

```
sench/
├── sench/
│   ├── __init__.py         # Exports
│   ├── __main__.py         # Entry point
│   ├── cli.py              # CLI principal
│   ├── core/
│   │   └── scraper.py      # Scraper combiné
│   ├── modules/
│   │   └── base.py         # ModuleKey, prompts
│   ├── prompts/
│   │   └── templates/      # Prompts par module (.md)
│   └── tools/
│       ├── page_scraper.py # Extraction contenu
│       ├── screenshot.py   # Capture screenshot
│       └── social_scraper.py # Liens sociaux
├── landing/                # Landing page
├── install.sh              # Script d'installation
├── pyproject.toml
└── README.md
```

## Conventions

### Git
- Branches : `feature/`, `fix/`, `chore/`
- Commits : Conventional commits (feat:, fix:, docs:, etc.)

### Code
- Python 3.11+
- Type hints obligatoires
- Docstrings pour fonctions publiques

## Commandes rapides

```bash
# Run CLI
python -m sench stripe.com

# Run avec module spécifique
python -m sench stripe.com --gtm

# Plusieurs modules
python -m sench stripe.com --funding --founders

# Sans screenshot
python -m sench stripe.com --no-screenshot

# Version
python -m sench --version
```

## Modules d'analyse

| Module | Flag | Description |
|--------|------|-------------|
| identity | `--identity` | Identité entreprise |
| funding | `--funding` | Levées de fonds |
| founders | `--founders` | Fondateurs et équipe |
| finance | `--finance` | Signaux financiers |
| icp | `--icp` | Ideal Customer Profile |
| product | `--product` | Produits et features |
| market | `--market` | Proposition de valeur |
| competitors | `--competitors` | Concurrents |
| gtm | `--gtm` | Go-to-Market |
| marketing | `--marketing` | Marketing et contenu |
| news | `--news` | Actualités |
| legal | `--legal` | Contexte légal |

Sans flag, tous les modules sont exécutés.

## Installation

```bash
# Via curl
curl -fsSL https://sench.ai/install | bash

# Manuel
pip install playwright
playwright install chromium
```
