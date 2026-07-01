# Checklist de test — CS GREFFE OS Learn

À utiliser à chaque déploiement ou changement notable sur Streamlit Cloud.

## Démarrage

- [ ] L'application démarre sans erreur.
- [ ] Aucune erreur ni exception visible dans les logs Streamlit Cloud au démarrage.
- [ ] La page d'accueil s'affiche correctement.

## Navigation

- [ ] Tous les liens et menus de navigation fonctionnent.
- [ ] Aucune page ne renvoie une erreur 404 ou un écran blanc.

## Contenu

- [ ] Seules des données fictives sont affichées (aucune donnée judiciaire réelle).
- [ ] Aucun secret ni clé API n'est visible dans l'interface ou le code source affiché.
- [ ] Les textes et modules e-learning s'affichent correctement (pas de contenu tronqué ou manquant).

## Fonctionnalités

- [ ] Les fonctionnalités principales du MVP répondent comme attendu.
- [ ] Les interactions utilisateur (boutons, formulaires, sélecteurs) fonctionnent sans erreur.

## Sécurité et gouvernance

- [ ] Aucune connexion Snowflake active constatée.
- [ ] Aucune connexion OpenAI active constatée.
- [ ] Aucune donnée sensible ou réelle n'a été introduite.

## Clôture

- [ ] Tout dysfonctionnement observé est documenté via le [modèle de rapport de bug](BUG_REPORT_TEMPLATE.md).
- [ ] Le résultat global du test (validé / bugs ouverts) est communiqué.
