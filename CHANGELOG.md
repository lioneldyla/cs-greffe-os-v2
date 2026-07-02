# Changelog — CS GREFFE OS

## 2026-07-02

### Audit et corrections (audit v1 appliqué)

**cs_greffe_os/app.py — fix(app)**
- Alignement du SCHEMA avec les colonnes réelles des CSV :
  - `students` : ajout `prenom`, `email`, `promotion`, `statut`
  - `scores` : ajout `date_eval`
  - `attempts` : ajout `correcte`, `score_obtenu`, `date_tentative`
- Suppression de l'appel dupliqué à `_chart_moyenne_module` dans `tab_overview`
- Ajout d'un filtre multiselect par promotion dans `tab_students`
- Ajout d'un filtre multiselect par date d'évaluation dans `tab_perf`
- Ajout de `use_container_width=True` sur tous les `st.dataframe`

**CI/CD — .github/workflows/ci.yml**
- Création du workflow GitHub Actions CI
- Exécution automatique sur push et PR vers `main`
- Steps : checkout, Python 3.11, install dépendances, `ruff check .`, `pytest tests/ -v`

**LDGP — living-digital-governance-platform/models/states/**
- Correction `STATE_TRANSITIONS.md` : fermeture du bloc mermaid manquant
- Création `LIFECYCLE_MATRIX.md` : matrice 7 objets × 7 états

**LDGP — living-digital-governance-platform/models/validation/**
- Correction `HUMAN_VALIDATION_MODEL.md` : fermeture du bloc mermaid manquant

## 2026-07-01

- Réorganisation : fusion de `data projects/CS GREFFE OS` (84 fichiers) et `data projects/CS_GREFFE_OS_TARGET_TREE_COMPLETE_SCAFFOLD` (99 fichiers) dans `ALLDATA/01_PROJETS_LOGICIELS/cs-greffe-os/` sous `docs_and_research/` et `scaffold/` respectivement.
- Copie vérifiée fichier par fichier (comptage identique source/destination). Dossiers sources originaux conservés en l'état, en attente de validation explicite avant suppression.
- Ajout d'un README de tête documentant la structure fusionnée et la dette documentaire identifiée (absence d'ARCHITECTURE.md, doublons docx/pdf non traités).
- Commit initial MVP : `cs_greffe_os/app.py`, données fictives CSV, documentation de test, modèles LDGP.
