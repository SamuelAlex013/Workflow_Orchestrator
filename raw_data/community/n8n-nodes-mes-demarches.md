# n8n-nodes-mes-demarches

Plugin n8n officiel pour l'intégration avec l'API **mes-démarches** (Polynésie française).

## 🎯 Fonctionnalités

- **Lister les dossiers** d'une démarche avec synchronisation intelligente
- **Consulter une démarche** et ses métadonnées
- **Consulter un dossier** individuel avec tous ses détails
- **Authentification sécurisée** par token API
- **Transformation des données** configurable (libellés originaux ou snake_case)
- **Optimisation des performances** avec requêtes stockées pré-configurées

## 📦 Installation

```bash
npm install n8n-nodes-mes-demarches
```

### Installation dans n8n

1. **Via l'interface n8n** (recommandé) :
   - Aller dans Settings → Community Nodes
   - Cliquer sur "Install a community node"
   - Entrer : `n8n-nodes-mes-demarches`

2. **Via ligne de commande** :
   ```bash
   # Installation globale
   npm install -g n8n-nodes-mes-demarches
   
   # Redémarrer n8n
   n8n start
   ```

3. **Docker** :
   ```dockerfile
   FROM n8nio/n8n
   RUN npm install -g n8n-nodes-mes-demarches
   ```

## 🔧 Configuration

### 1. Créer les identifiants API

1. Dans n8n, aller dans **Credentials** → **Add Credential**
2. Rechercher "**API mes-démarches**"
3. Remplir :
   - **Serveur** : `https://www.mes-demarches.gov.pf` (par défaut)
   - **Token API** : Votre token d'accès GraphQL

### 2. Obtenir un token API

Pour obtenir un token d'accès à l'API mes-démarches :

1. Connectez-vous sur [mes-demarches.gov.pf](https://www.mes-demarches.gov.pf)
2. Accédez à votre profil administrateur
3. Générez un nouveau token API dans la section dédiée
4. Copiez le token (il ne sera affiché qu'une seule fois)

## 🚀 Utilisation

### Opérations disponibles

#### 1. Lister les dossiers

Récupère tous les dossiers d'une démarche avec synchronisation intelligente.

**Paramètres principaux :**
- **Numéro de démarche** : ID de la procédure à consulter
- **Mode de synchronisation** : 
  - *Auto* (recommandé) : Reprend depuis la dernière synchronisation
  - *Date spécifique* : Depuis une date donnée
  - *Tous les dossiers* : Synchronisation complète
- **État des dossiers** : Filtrer par statut (accepté, refusé, en instruction, etc.)
- **Format des attributs** : Libellés originaux (pour Baserow) ou snake_case

#### 2. Consulter une démarche

Récupère les métadonnées et la structure d'une démarche.

**Paramètres :**
- **Numéro de démarche** : ID de la procédure
- **Inclure les groupes instructeurs** : Informations sur les agents
- **Inclure le service** : Détails du service gestionnaire
- **Inclure la révision** : Structure des champs du formulaire

#### 3. Consulter un dossier

Récupère les détails complets d'un dossier spécifique.

**Paramètres :**
- **Numéro de dossier** : ID du dossier à consulter
- **Format des attributs** : Format de sortie des données
- **Options d'inclusion** : Champs, annotations, traitements, messages, etc.

### Exemple de workflow

```json
{
  "nodes": [
    {
      "name": "Mes-Démarches",
      "type": "n8n-nodes-mes-demarches.mesDemarches",
      "parameters": {
        "operation": "listDossiers",
        "demarcheNumber": 123,
        "syncMode": "auto",
        "state": "en_instruction",
        "attributeFormat": "original"
      },
      "credentials": {
        "mesDemarchesApi": "mes-demarches-prod"
      }
    }
  ]
}
```

## 🔄 Synchronisation intelligente

Le plugin offre trois modes de synchronisation :

### Mode Auto (Recommandé)
- Détecte automatiquement la dernière synchronisation réussie
- Récupère uniquement les dossiers modifiés depuis
- Optimal pour les synchronisations régulières

### Mode Date spécifique
- Permet de spécifier manuellement une date de début
- Utile pour la synchronisation ponctuelle ou de rattrapage

### Mode Complet
- Récupère tous les dossiers de la démarche
- À utiliser avec précaution pour les grosses procédures

## 📊 Transformation des données

### Format des attributs

**Libellés originaux** (recommandé pour Baserow) :
```json
{
  "champs": {
    "Nom de famille": "Dupont",
    "Date de naissance": "1990-01-15",
    "Adresse e-mail": "jean.dupont@email.com"
  }
}
```

**Format snake_case** (pour intégrations techniques) :
```json
{
  "champs": {
    "nom_de_famille": "Dupont",
    "date_de_naissance": "1990-01-15",
    "adresse_e_mail": "jean.dupont@email.com"
  }
}
```

## ⚡ Performances

Le plugin utilise les **requêtes stockées** optimisées de l'API mes-démarches :
- Réduction du temps de réponse
- Diminution de la charge serveur
- Meilleure fiabilité des requêtes

## 🔒 Sécurité

- Authentification par token Bearer sécurisé
- Test de connectivité automatique
- Gestion d'erreurs robuste
- Respect des bonnes pratiques n8n

## 🐛 Dépannage

### Le plugin n'apparaît pas dans n8n

1. Vérifiez l'installation : `npm list -g n8n-nodes-mes-demarches`
2. Redémarrez n8n complètement
3. Vérifiez les logs n8n pour les erreurs de chargement

### Erreur de token invalide

1. Vérifiez que le token est correct et actif
2. Testez la connectivité depuis les paramètres des identifiants
3. Assurez-vous que l'URL du serveur est correcte

### Performances lentes

1. Utilisez le mode de synchronisation "Auto" au lieu de "Tous les dossiers"
2. Limitez les options d'inclusion (messages, géométrie) si non nécessaires
3. Filtrez par état de dossier pour réduire le volume

## 📚 API et Documentation

- [Documentation officielle mes-démarches](https://doc.demarches-simplifiees.fr/graphql-api)
- [Guide n8n Community Nodes](https://docs.n8n.io/integrations/community-nodes/)

## 🤝 Contribution

Ce plugin est développé spécifiquement pour les besoins de la Polynésie française.

### Développement local

```bash
# Cloner le projet
git clone https://github.com/your-org/n8n-nodes-mes-demarches.git
cd n8n-nodes-mes-demarches

# Installer les dépendances
npm install

# Compiler
npm run build

# Tests
npm test

# Linter
npm run lint
```

## 📄 Licence

MIT

## 📞 Support

Pour le support technique et les questions spécifiques à la Polynésie française, contactez : contact@service-public.pf

---

**Développé avec ❤️ pour la Polynésie française**