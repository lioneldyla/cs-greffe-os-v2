# Architecture -- CS GREFFE OS Learn

## Vue d'ensemble

Prototype cloud e-learning pour l'INFJ (Institut National de Formation Judiciaire de Cote d'Ivoire).
Stack : Python 3.11+ / Streamlit / Pandas / Plotly / CSV de donnees fictives.

## Structure du depot

```
cs-greffe-os-v2/
|-- cs_greffe_os/          # Application principale (entree Streamlit)
|   |-- app.py             # Point d'entree : streamlit run cs_greffe_os/app.py
|   |-- data/              # CSV de demonstration (donnees fictives)
|-- 02_MVP_EXECUTABLE/     # Arborescence V1 de scaffolding (reference, non active)
|   |-- 03_CORPUS/         # Corpus documentaire en construction
|   |-- feedback/          # Journaux d'usage et retours
|-- docs/                  # Documentation projet et plan de test
|   |-- testing/           # TEST_PLAN.md, checklist, modele bug report
|-- docs_and_research/     # Materiaux de recherche fusionnes
|-- living-digital-governance-platform/models/  # Modeles de gouvernance LDGP
|-- scaffold/              # Constitution et regles du projet
|-- scripts/               # Outils de scaffolding
|-- tests/docs/            # Tests pytest sur les modeles LDGP
|-- source_materials/      # Sources primaires (en attente)
|-- ARCHITECTURE.md        # Ce fichier
|-- CHANGELOG.md
|-- README.md
|-- requirements.txt       # streamlit / pandas / plotly (versions pinnees)
|-- .gitignore
```

## Entree de l'application

```bash
cd cs-greffe-os-v2
pip install -r requirements.txt
streamlit run cs_greffe_os/app.py
```

## Modele de donnees (CSV fictifs)

Les tables sont dans `cs_greffe_os/data/` :

- `modules.csv` -- modules d'apprentissage
- - `students.csv` -- apprenants fictifs
  - - `scores.csv` -- resultats par module et etudiant (colonnes : score, progression)
    - - `lessons.csv` -- lecons par module
      - - `questions.csv` -- questions par lecon
        - - `attempts.csv` -- tentatives de reponse
          - - `corrections.csv` -- corrections des tentatives
            - - `sources.csv` -- sources documentaires par module
              - - `audit_logs.csv` -- journal d'audit fictif
               
                - ## Exclusions MVP Release 0.1
               
                - - Pas de donnees judiciaires reelles
                  - - Pas de connexion Snowflake ou OpenAI
                    - - Pas d'agents autonomes
                      - - Pas de remplacement du greffier ou du magistrat
                       
                        - ## Dette technique connue
                       
                        - Voir `docs/testing/TEST_PLAN.md` et `CHANGELOG.md` pour le suivi.
                        - 
