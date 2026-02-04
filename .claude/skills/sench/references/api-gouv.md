# API Recherche Entreprises

API publique du gouvernement francais. **Aucune cle API requise.**

## Endpoint

```
GET https://recherche-entreprises.api.gouv.fr/search?q={query}&page=1&per_page=5
```

## Parameters

| Param | Description |
|-------|-------------|
| `q` | Search query (name, SIREN, or SIRET) |
| `page` | Page number (default: 1) |
| `per_page` | Results per page (default: 10, max: 25) |

## Response Fields

In `results[]`:

```json
{
  "siren": "443061841",
  "nom_complet": "ALAN",
  "nom_raison_sociale": "ALAN",
  "date_creation": "2016-02-25",
  "nature_juridique": "5710",
  "activite_principale": "65.12Z",
  "tranche_effectif_salarie": "42",
  "categorie_entreprise": "ETI",
  "siege": {
    "adresse": "12 RUE GODOT DE MAUROY",
    "code_postal": "75009",
    "commune": "PARIS 9"
  },
  "dirigeants": [
    {
      "nom": "MEYERS",
      "prenoms": "Charles",
      "qualite": "Président"
    }
  ],
  "finances": {
    "2023": {
      "ca": 50000000,
      "resultat_net": -5000000
    }
  }
}
```

## Key Fields

| Field | Description |
|-------|-------------|
| `siren` | 9-digit company identifier |
| `nom_complet` | Full company name |
| `date_creation` | Creation date (YYYY-MM-DD) |
| `nature_juridique` | Legal form code |
| `activite_principale` | NAF/APE activity code |
| `tranche_effectif_salarie` | Employee range code |
| `categorie_entreprise` | PME, ETI, or GE |
| `siege` | Headquarters address |
| `dirigeants[]` | Directors list |
| `finances` | Financial data (if available) |

## Employee Range Codes

| Code | Range |
|------|-------|
| 00 | 0 |
| 01 | 1-2 |
| 02 | 3-5 |
| 03 | 6-9 |
| 11 | 10-19 |
| 12 | 20-49 |
| 21 | 50-99 |
| 22 | 100-199 |
| 31 | 200-249 |
| 32 | 250-499 |
| 41 | 500-999 |
| 42 | 1000-1999 |
| 51 | 2000-4999 |
| 52 | 5000-9999 |
| 53 | 10000+ |

## Example Usage

```bash
# Search by name
WebFetch: https://recherche-entreprises.api.gouv.fr/search?q=alan&page=1&per_page=5

# Search by SIREN
WebFetch: https://recherche-entreprises.api.gouv.fr/search?q=443061841&page=1&per_page=5
```
