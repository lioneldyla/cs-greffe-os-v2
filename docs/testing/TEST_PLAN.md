# Plan de test — CS GREFFE OS Learn

## Objectif

Définir le périmètre et l'approche de test du MVP CS GREFFE OS Learn (application e-learning cloud pour l'INFJ) avant toute mise à disposition élargie.

## Périmètre

- Application Streamlit du MVP e-learning.
- Parcours utilisateur : navigation, consultation des modules, contenus fictifs.
- Aucune donnée judiciaire réelle n'est utilisée dans les tests.
- Aucune connexion Snowflake ou OpenAI n'est testée : elles ne sont pas actives dans ce MVP.

## Types de tests

1. **Test de fumée (smoke test)** — l'application démarre sans erreur.
2. **Test fonctionnel** — les fonctionnalités principales du MVP répondent comme attendu.
3. **Test de non-régression** — les fonctionnalités déjà validées restent opérationnelles après une modification.
4. **Test de contenu** — vérifier que seules des données fictives sont affichées.

## Environnement de test

- Déploiement : Streamlit Cloud.
- Données : jeux de données fictifs uniquement.
- Accès : aucun secret ni clé API requis pour ce MVP.

## Méthode

1. Suivre la [checklist de test](TEST_CHECKLIST.md) à chaque déploiement ou changement notable.
2. Documenter tout dysfonctionnement avec le [modèle de rapport de bug](BUG_REPORT_TEMPLATE.md).
3. Valider humainement chaque anomalie avant correction — aucune action corrective automatisée par IA.

## Critères de sortie

- Tous les éléments de la checklist sont validés.
- Aucun bug bloquant ouvert.
- Aucune donnée réelle ou secret détecté dans l'application ou le dépôt.
