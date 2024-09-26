### **Projet : Système d'Identification de Voix**

**Participants :**
- Abdou Samath Seck
- Dorian Lovichi

#### **Description du projet :**
L'objectif de ce projet est de développer une intelligence artificielle (IA) capable d'identifier une voix et de l'associer à un utilisateur précis. Ce système pourrait être utilisé dans divers cas d'utilisation tels que l'authentification sécurisée, la reconnaissance d'utilisateurs dans des applications vocales ou encore la personnalisation d'interactions en fonction des utilisateurs.

Le projet s'appuiera sur les technologies suivantes :
- **Django** (pour la partie serveur et la gestion de la base de données).
- **Vosk API** (pour la reconnaissance vocale hors ligne).

#### **Technologies utilisées :**
1. **Django** :  
   - **Framework Python** open source pour le développement web qui permettra de gérer la partie serveur et l'interaction avec la base de données.
   - Django sera utilisé pour :
     - La gestion des utilisateurs.
     - L'hébergement de l'application.
     - La création d'interfaces permettant d'ajouter de nouvelles voix et de gérer les profils utilisateurs.

2. **Vosk API** :  
   - Bibliothèque de reconnaissance vocale open source qui fonctionne **hors ligne**.
   - Elle est légère, rapide, et compatible avec plusieurs langages, dont **Python**.
   - Vosk supporte plus de 20 langues, ce qui permettra une flexibilité linguistique dans les applications futures.
   - Elle est compatible avec des systèmes légers tels que **Raspberry Pi**, ce qui ouvre la voie à l'implémentation du projet sur des dispositifs embarqués.
   - L'API Vosk sera utilisée pour :
     - **Capturer la voix d'un utilisateur**.
     - **Convertir la voix en texte** pour des besoins d'analyse.
     - **Créer un profil vocal unique** pour chaque utilisateur afin de permettre l'identification.

#### **Fonctionnalités prévues :**
1. **Enregistrement de la voix** :
   - Lorsqu'un utilisateur s'enregistre pour la première fois, il devra fournir un échantillon vocal.
   - Cet échantillon sera analysé et utilisé pour créer un **profil vocal unique**.
   
2. **Identification de la voix** :
   - Lorsqu'un utilisateur parlera, le système identifiera la voix et la comparera aux profils existants pour déterminer qui est en train de parler.
   - Si la voix correspond à un utilisateur existant, le système l'authentifiera automatiquement.

3. **Base de données des profils utilisateurs** :
   - Django permettra de stocker les **profils utilisateurs** ainsi que les **modèles vocaux** associés.
   - Chaque utilisateur aura un **ID unique**, qui sera lié à son modèle vocal.

4. **Reconnaissance multi-utilisateurs** :
   - Le système pourra gérer plusieurs utilisateurs et identifier la voix de chacun d'eux sans confusion, ce qui pourrait être utile pour des environnements partagés (par exemple, des maisons intelligentes, des bureaux, etc.).

5. **Interface utilisateur** :
   - Une interface web simple permettra aux utilisateurs de s'enregistrer, de gérer leur profil et de visualiser les résultats des identifications vocales.

#### **Étapes de développement :**
1. **Mise en place de l'environnement de développement** :
   - Installer Django et configurer le projet.
   - Installer Vosk et tester son intégration dans l'application Python.
   
2. **Développement des fonctionnalités d'enregistrement de voix** :
   - Créer une interface pour que l'utilisateur puisse soumettre un échantillon vocal.
   - Stocker cet échantillon dans un format utilisable (par exemple, WAV ou MP3).

3. **Création des modèles utilisateurs** :
   - Développer une base de données dans Django pour gérer les utilisateurs et leurs profils vocaux.

4. **Intégration de Vosk pour la reconnaissance vocale** :
   - Implémenter la logique permettant à Vosk de capturer la voix en temps réel.
   - Développer un algorithme de comparaison des voix pour permettre l'identification.

5. **Test et validation** :
   - Tester l'identification vocale avec plusieurs utilisateurs et voix différentes.
   - Optimiser les performances du système, en particulier pour les environnements légers comme Raspberry Pi.

6. **Interface utilisateur** :
   - Développer une interface web pour l'enregistrement et la gestion des utilisateurs.
   
7. **Déploiement** :
   - Déployer l'application sur un serveur et la tester dans un environnement réel.


#### **Outils et bibliothèques supplémentaires :**
- **SQLite ou PostgreSQL** pour la base de données des utilisateurs.
- **Nginx** ou **Apache** pour le déploiement du serveur Django.
- **Pyaudio** ou toute autre bibliothèque Python pour capturer et traiter les entrées audio.


