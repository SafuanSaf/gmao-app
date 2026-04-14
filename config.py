import os

# =============================================================
# CONFIGURATION GLOBALE DE L'APPLICATION GMAO
# =============================================================

# Chemin de base : répertoire où se trouve ce fichier (= racine du projet)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Chemin vers la base de données Excel (même dossier que l'application)
DB_PATH = os.path.join(BASE_DIR, "GMAO_DATABASE.xlsx")

# Chemin vers le dossier de backups
BACKUP_DIR = os.path.join(BASE_DIR, "BACKUPS_GMAO")

# Clé secrète Flask pour les sessions (à changer en production)
SECRET_KEY = "gmao-secret-key-2024-change-moi"

# Délai max de retry pour l'accès en écriture à la DB (en secondes)
DB_LOCK_TIMEOUT = 10

# Timeouts pour la veille web (en secondes)
VEILLE_TIMEOUT = 5

# =============================================================
# STRUCTURE DE LA BASE DE DONNÉES EXCEL
# =============================================================

# Nom des onglets
SHEET_DONNEES    = "Données"
SHEET_CATALOGUE  = "CATALOGUE_MAITRE"
SHEET_LISTES     = "LISTES"
SHEET_USERS      = "USERS"
SHEET_LOGS       = "LOGS"
SHEET_ALERTES    = "ALERTES_VEILLE"

# Colonnes de l'onglet "Données" (index 0-based)
COL_D_MACHINE       = 0   # Col A  : Machine
COL_D_SOUS_ENS      = 1   # Col B  : Sous-Ensemble
COL_D_TYPE_COM      = 2   # Col C  : Type Composant
COL_D_DESIGNATION   = 3   # Col D  : Désignation (calculée)
COL_D_QTE           = 4   # Col E  : Quantité
COL_D_FABRICANT     = 5   # Col F  : Fabricant (calculé)
COL_D_REFERENCE     = 6   # Col G  : Référence (clé technique)
COL_D_STATUT_SITE   = 7   # Col H  : Statut Site (calculé)
COL_D_STATUT_CYCLE  = 8   # Col I  : Statut Cycle de Vie (calculé)
COL_D_LIEN_PROD     = 9   # Col J  : Lien Produit (calculé)
COL_D_SUCCESSEUR    = 10  # Col K  : Successeur? (calculé)
COL_D_DESIG_REMP    = 11  # Col L  : Désignation Remplaçant (calculé)
COL_D_REF_REMP      = 12  # Col M  : Référence Remplaçant (calculé)
COL_D_FAB_REMP      = 13  # Col N  : Fabricant Remplaçant (calculé)
COL_D_STATUT_SITE_R = 14  # Col O  : Statut Site Remplaçant (calculé)
COL_D_STATUT_REMP   = 15  # Col P  : Statut Remplaçant (calculé)
COL_D_LIEN_REMP     = 16  # Col Q  : Lien Remplaçant (calculé)
COL_D_COMMENTAIRE   = 17  # Col R  : Commentaire

# Colonnes de l'onglet "CATALOGUE_MAITRE" (index 0-based)
COL_C_REFERENCE     = 0   # Col A  : Référence
COL_C_FABRICANT     = 1   # Col B  : Fabricant
COL_C_DESIGNATION   = 2   # Col C  : Désignation
COL_C_STATUT_SITE   = 3   # Col D  : Statut SITE
COL_C_STATUT_INT    = 4   # Col E  : Statut INTERNE
COL_C_LIEN_PROD     = 5   # Col F  : Lien Produit
COL_C_SUCCESSEUR    = 6   # Col G  : Successeur? (OUI/NON)
COL_C_REF_REMP      = 7   # Col H  : Ref Remplaçant
COL_C_FAB_REMP      = 8   # Col I  : Fab Remplaçant
COL_C_DESIG_REMP    = 9   # Col J  : Desig Remplaçant
COL_C_STATUT_SITE_R = 10  # Col K  : Statut SITE Remp
COL_C_STATUT_INT_R  = 11  # Col L  : Statut INT Remp
COL_C_LIEN_REMP     = 12  # Col M  : Lien Remplaçant

# Colonnes de l'onglet "LISTES" (index 0-based)
COL_L_FABRICANTS    = 0   # Col A
COL_L_MACHINES      = 1   # Col B
COL_L_TYPES         = 2   # Col C
COL_L_STATUTS       = 3   # Col D
COL_L_OUINON        = 4   # Col E

# Colonnes de l'onglet "USERS" (index 0-based)
COL_U_LOGIN         = 0   # Col A  : Identifiant
COL_U_PASSWORD      = 1   # Col B  : Mot de passe
COL_U_ROLE          = 2   # Col C  : Rôle (ADMIN / USER)
COL_U_FIRST_LOGIN   = 3   # Col D  : Premier login (OUI/NON)

# Colonnes de l'onglet "LOGS" (index 0-based)
COL_LOG_DATE        = 0   # Col A  : Horodatage
COL_LOG_USER        = 1   # Col B  : Utilisateur
COL_LOG_ACTION      = 2   # Col C  : Action
COL_LOG_DETAIL      = 3   # Col D  : Détail

# Colonnes de l'onglet "ALERTES_VEILLE" (index 0-based)
COL_AV_DATE         = 0   # Col A  : Date détection
COL_AV_REFERENCE    = 1   # Col B  : Référence
COL_AV_STATUT_FICH  = 2   # Col C  : Statut dans fichier
COL_AV_STATUT_WEB   = 3   # Col D  : Statut détecté sur le web
COL_AV_URL          = 4   # Col E  : URL analysée
