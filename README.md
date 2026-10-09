# Projet 03 — Contrôle de conformité à la charia

Application académique développée en Python avec Streamlit dans le cadre d’un mémoire consacré à l’économie islamique et aux risques de la mourabaha.

## Objectif

L’application propose une liste de contrôle fondée sur quatre critères :

- La propriété et la possession du véhicule par la banque avant sa vente au client.
- L’antériorité de la date de possession par rapport à celle du contrat de vente.
- L’absence d’intérêts de retard.
- La clarté des frais prévus dans le contrat.

## Fonctionnement

L’utilisateur renseigne les quatre critères, puis demande le rapport de contrôle.

Lorsque tous les critères sont cochés, l’application indique leur validation. Dans le cas contraire, elle affiche les critères non satisfaits et les observations correspondantes.

## Fichiers

- `audit.py` : interface et règles de contrôle.
- `requirements.txt` : dépendance nécessaire au fonctionnement.

## Installation et lancement

Depuis le dossier du projet :

```bash
python -m pip install -r requirements.txt
python -m streamlit run audit.py
```

## Portée

Le contrôle repose sur les réponses saisies par l’utilisateur. L’application constitue un outil pédagogique d’aide à la vérification ; elle ne réalise pas une lecture automatique des contrats et ne remplace pas l’examen d’une instance compétente en matière de conformité à la charia.
