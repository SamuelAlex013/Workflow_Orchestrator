![n8n-nodes-starter](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# MakeHub AI n8n Node

Ce dépôt contient le nœud personnalisé **MakeHub AI** pour n8n, permettant d’interagir avec l’API MakeHub AI LLM. Grâce à ce nœud, vous pouvez envoyer des messages de chat à un modèle LLM, transformer dynamiquement leur contenu et ajuster des paramètres de performance pour optimiser vos requêtes.

## Fonctionnalités

- **Interaction de Chat** : Envoyez des messages à l’API MakeHub AI pour obtenir des réponses générées par un modèle LLM.
- **Transformation Dynamique des Messages** : Évaluez des expressions intégrées dans le contenu des messages pour personnaliser vos requêtes.
- **Paramètres de Performance** : Configurez le débit minimum (tokens/sec) et la latence maximale (ms) pour optimiser vos échanges.
- **Champs Additionnels Personnalisables** : Ajustez le nombre maximal de tokens, la température (pour contrôler la variabilité) et activez ou non le mode stream.

## Prérequis

Avant d’utiliser ce nœud, assurez-vous d’avoir installé :

- [n8n](https://n8n.io) – (Consultez la [documentation officielle](https://docs.n8n.io/) pour l’installation et la configuration.)
- Node.js (version 18 minimum) et pnpm.
- [Git](https://git-scm.com/downloads).

## Installation

1. **Cloner le dépôt :**

   ```sh
   git clone https://github.com/Remenby31/makehub-n8n-node.git
   ```

2. **Installer les dépendances :**

   ```sh
   pnpm install
   ```

3. **Construire et configurer le nœud :**

   Adaptez et compilez le nœud selon vos besoins. Pour cela, reportez-vous à la [documentation n8n sur le développement de nœuds](https://docs.n8n.io/integrations/creating-nodes/build/node-development-environment/).

## Configuration

### Credentials

Le nœud **MakeHub AI** nécessite des credentials valides pour l’API MakeHub. Créez un credential nommé **makeHubApi** comportant :

- **API Key** : Votre clé API MakeHub.

Assurez-vous de configurer ces credentials dans n8n. Pour plus d’informations, consultez la [documentation sur les credentials](https://docs.n8n.io/integrations/creating-nodes/credentials/).

### Paramètres du Nœud

Lors de la configuration du nœud dans votre workflow, vous trouverez les options suivantes :

- **Resource** : Fixé à `Chat`.
- **Operation** : `Message Model` – Permet d’envoyer des messages à un modèle LLM.
- **Model Name or ID** : Sélectionnez ou spécifiez l’identifiant du modèle LLM à utiliser.
- **Messages** : Ajoutez un ou plusieurs messages à envoyer. Chaque message comporte :
  - **Role** : Le rôle de l’expéditeur (`assistant`, `system` ou `user`).
  - **Content** : Le contenu du message. Ce champ supporte les expressions pour une évaluation dynamique.
  
### Paramètres de Performance

Les nouveaux paramètres de performance se trouvent désormais sous deux sections distinctes :

- **Min Throughput Settings** : 
  - **Min Throughput Mode** : Choisissez entre :
    - **Best Price** : le paramètre n’est pas envoyé.
    - **Custom Value** : envoie la valeur numérique saisie (par défaut 40 tokens/sec).
    - **Best Performance** : envoie la chaîne `"best"`.
  - Si vous choisissez **Custom Value**, un champ vous permet de définir la valeur souhaitée.

- **Max Latency Settings** :
  - **Max Latency Mode** : Choisissez entre :
    - **Best Price** : le paramètre n’est pas envoyé.
    - **Custom Value** : envoie la valeur numérique saisie (par défaut 1000 millisecondes).
    - **Best Performance** : envoie la chaîne `"best"`.
  - Si vous choisissez **Custom Value**, un champ vous permet de définir la valeur souhaitée.

### Simplify Output

Le paramètre **Simplify Output** est désormais géré en dehors des champs additionnels.  
- Si activé, seul le contenu généré par le modèle (situé dans `response.choices[0].message.content`) sera retourné.  
- Sinon, la réponse complète de l’API sera transmise.

---

Ces options permettent de choisir finement entre l’optimisation du prix et la performance, ainsi qu’un mode de sortie simplifié pour une intégration plus fluide.

## Exemple d’Utilisation

1. **Créez un nouveau workflow dans n8n.**
2. **Ajoutez le nœud MakeHub AI** et configurez-le avec vos paramètres souhaités.
3. **Configurez les credentials** (**makeHubApi**) avec votre clé API MakeHub.
4. **Intégrez le nœud** dans votre workflow pour traiter et exploiter les réponses de l’API MakeHub.

## Tests et Débogage

Testez votre nœud en local en suivant les conseils de la [documentation sur l’exécution locale des nœuds](https://docs.n8n.io/integrations/creating-nodes/test/run-node-locally/). Les logs détaillés (via LoggerProxy) vous aideront à déboguer et suivre l’exécution de chaque étape.

## Personnalisation

Vous pouvez adapter le code du nœud (situé dans le répertoire `/nodes`) pour répondre à vos besoins spécifiques. Pensez à mettre à jour le fichier `package.json` et cette documentation en conséquence.

## Publication

Une fois testé et validé, vous pouvez publier ce nœud sous forme de package npm pour le partager avec la communauté n8n. Reportez-vous aux [guidelines de publication sur npm](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry).

## Licence

Ce projet est sous licence [MIT](LICENSE).

---

Pour plus d’informations sur la création de nœuds personnalisés pour n8n, consultez la [documentation officielle](https://docs.n8n.io/integrations/creating-nodes/).

