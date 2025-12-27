# 🛡️ SOC AI Assistant

**Assistant intelligent pour la détection et l'analyse d'attaques cybernétiques autonomes propulsées par l'IA**

## 📋 Vue d'ensemble du projet

Ce projet développe un système d'assistance pour Security Operations Center (SOC) capable de détecter et analyser les cyberattaques orchestrées par l'intelligence artificielle, directement inspiré du rapport Anthropic de novembre 2025 sur la première campagne de cyber-espionnage orchestrée par IA (GTG-1002).

### Contexte

Le rapport Anthropic révèle qu'un groupe sponsorisé par un État a utilisé Claude Code pour mener des attaques où l'IA exécutait **80-90% des opérations tactiques de manière autonome** :
- Reconnaissance automatisée des infrastructures
- Découverte et exploitation de vulnérabilités
- Mouvement latéral dans les réseaux
- Extraction et analyse de données sensibles
- Rythme d'attaque surhumain (plusieurs opérations par seconde)

### Objectif

Développer un système défensif qui :
1. **Détecte** les patterns d'attaques autonomes pilotées par IA
2. **Analyse** les alertes de sécurité avec contexte MITRE ATT&CK
3. **Recommande** des actions de réponse aux analystes SOC
4. **Automatise** le triage des alertes pour réduire la charge cognitive

## 🎯 Phases du projet

### Phase 1 : MVP avec alertes simulées (EN COURS - 95% COMPLÉTÉ)
- ✅ Analyse d'alertes JSON simulées
- ✅ Intégration Ollama (Llama 3.2) en local
- ✅ Construction de prompts structurés pour analyse SOC
- ✅ Communication avec API Ollama (POST requests)
- ✅ Gestion d'erreurs robuste avec try/except
- ✅ Analyse en batch d'alertes multiples avec enumerate()
- ✅ Fonction main() complète pour orchestration
- ✅ Chargement JSON avec gestion d'erreurs
- ✅ Affichage de progression [x/total]
- ✅ Sauvegarde automatique des résultats dans logs/
- ✅ Statistiques de synthèse par sévérité
- ✅ **Base de données MITRE ATT&CK** (11 techniques avec indicateurs et recommandations)
- ✅ **Fonctions utilitaires MITRE** (recherche par ID, indicateur, tactique, sévérité)
- 🔄 Détection de patterns d'attaque IA (en cours d'affinement)
- 🔄 Intégration de la base MITRE dans l'analyseur (à venir)
- 🎯 **Coût : 0€** (100% local)

### Phase 2 : Intégration IDS réel
- 🔄 Déploiement Suricata (IDS open-source)
- 🔄 Ingestion temps réel des alertes
- 🔄 Corrélation d'événements
- 🔄 Interface web Flask
- 🎯 **Coût : 0-5€/mois** (VPS optionnel)

### Phase 3 : SOC Automation avancé
- ⏳ Orchestration de réponses avec Ansible
- ⏳ Playbooks automatisés
- ⏳ Dashboard Grafana
- ⏳ API publique
- 🎯 **Coût : 10-30€/mois**

## 🗂️ Architecture technique

```
┌─────────────────────────────────────────────────────────┐
│                     Phase 1 (MVP)                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  [Alertes JSON: data/sample_alerts.json]               │
│           ↓                                             │
│  [main() - Orchestration]                              │
│           ↓                                             │
│  [load_alerts_from_file() - Chargement sécurisé]      │
│           ↓                                             │
│  [analyze_batch() - Boucle avec enumerate()]           │
│           ↓                                             │
│  [build_prompt() - Prompt adaptatif]                   │
│           ↓                                             │
│  [mitre_database.py - Base de connaissances MITRE]     │
│           ↓                                             │
│  [send_to_ollama() - API Ollama → Llama 3.2 local]     │
│           ↓                                             │
│  [Analyse + Classification MITRE + Recommandations]    │
│           ↓                                             │
│  [save_results() - Export JSON horodaté]               │
│           ↓                                             │
│  [Affichage CLI + Statistiques par sévérité]          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Stack technique

| Composant | Technologie | Justification |
|-----------|-------------|---------------|
| **LLM** | Ollama + Llama 3.2 | Local, gratuit, optimisé Apple Silicon |
| **Langage** | Python 3.10+ | Écosystème ML/Sec robuste |
| **IDS** (Phase 2) | Suricata | Open-source, performant |
| **Conteneurisation** | Docker | Isolation et reproductibilité |
| **Orchestration** (Phase 3) | Ansible | Standard industrie |
| **Visualisation** (Phase 3) | Grafana | Dashboards SOC |

## 🔧 Setup de l'environnement

### Prérequis

- **OS** : macOS (Apple Silicon M1/M2/M3) ou Linux
- **RAM** : 16 GB minimum (recommandé pour Llama 3.2)
- **Disk** : 10 GB libres
- **Docker Desktop** : Installé et fonctionnel
- **Python** : 3.10 ou supérieur

### Installation complète

#### 1. Installation d'Ollama

```bash
# Via Homebrew (macOS)
brew install ollama

# Vérification
ollama --version

# Lancement du serveur Ollama (garder ce terminal ouvert)
ollama serve
```

#### 2. Téléchargement du modèle Llama 3.2

Dans un **nouveau terminal** :

```bash
# Télécharge Llama 3.2 (environ 2 GB)
ollama pull llama3.2

# Vérification
ollama list

# Test rapide
ollama run llama3.2 "Explique ce qu'est une attaque par force brute SSH"
```

#### 3. Clone et setup du projet

```bash
# Création de la structure
mkdir ~/soc-ai-assistant
cd ~/soc-ai-assistant

# Structure des dossiers
mkdir -p data logs scripts config

# Fichiers principaux
touch scripts/analyzer.py
touch data/sample_alerts.json
```

#### 4. Configuration Python

```bash
# Création environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Sur macOS/Linux

# Installation des dépendances
pip install requests

# Vérification
python --version  # Doit afficher Python 3.10+
```

#### 5. Ajout des fichiers du projet

Copier les fichiers suivants dans leurs emplacements respectifs :
- `data/sample_alerts.json` → Alertes simulées (8 scénarios d'attaque)
- `scripts/analyzer.py` → Script principal d'analyse
- `scripts/mitre_database.py` → Base de données MITRE ATT&CK

**Structure actuelle du code** :

**`scripts/analyzer.py`** - Script principal d'analyse :
```python
# Fonctions principales implémentées :
build_prompt(alert)              # Construit un prompt adaptatif avec .get()
send_to_ollama(prompt)           # Envoie le prompt à l'API Ollama locale
load_alerts_from_file(path)      # Charge les alertes avec gestion d'erreurs
analyze_batch(alerts)            # Analyse multiple avec enumerate(start=1)
save_results(results, path)      # Sauvegarde JSON horodatée
main()                           # Orchestration complète + statistiques
```

**`scripts/mitre_database.py`** - Base de données MITRE ATT&CK :
```python
# Base de données des techniques MITRE ATT&CK
MITRE_TECHNIQUES                 # Dict contenant 11 techniques avec indicateurs et recommandations

# Fonctions utilitaires :
get_technique(technique_id)                    # Récupère une technique par ID
search_by_indicator(keyword)                  # Recherche par mot-clé dans les indicateurs
get_techniques_by_tactic(tactic)              # Filtre par tactique MITRE
get_high_severity_techniques(threshold)       # Techniques haute sévérité (≥8)
get_database_stats()                          # Statistiques de la base
```

**Techniques MITRE couvertes** :
- **Reconnaissance** : T1046 (Network Service Discovery), T1595 (Active Scanning)
- **Credential Access** : T1110 (Brute Force), T1078 (Valid Accounts), T1555 (Credentials from Password Stores)
- **Lateral Movement** : T1021 (Remote Services)
- **Exfiltration** : T1041 (Exfiltration Over C2 Channel), T1048 (Exfiltration Over Alternative Protocol)
- **Execution** : T1059 (Command and Scripting Interpreter)
- **Initial Access** : T1190 (Exploit Public-Facing Application)
- **Command and Control** : T1071 (Application Layer Protocol)

Chaque technique inclut :
- Nom, tactique, description
- Score de sévérité (1-10)
- Liste d'indicateurs pour détection
- Recommandations d'action immédiate

#### 6. Lancement du système

```bash
# Terminal 1 : Ollama doit tourner
ollama serve

# Terminal 2 : Lancement de l'analyse
cd ~/soc-ai-assistant
source venv/bin/activate
python scripts/analyzer.py
```

### Commandes utiles

```bash
# Activer l'environnement Python
source venv/bin/activate

# Désactiver l'environnement
deactivate

# Vérifier les modèles Ollama disponibles
ollama list

# Supprimer un modèle (libérer espace)
ollama rm llama3.2

# Logs Ollama
tail -f ~/.ollama/logs/server.log

# Analyser toutes les alertes (main() le fait par défaut)
python scripts/analyzer.py

# Voir les résultats sauvegardés
cat logs/analysis_results.json | python -m json.tool

# Tester la base de données MITRE
python scripts/mitre_database.py
```

## 🤔 Pourquoi exécuter le LLM en local ?

### Avantages techniques

1. **Coût 0€**
   - Pas de frais d'API (Claude API : ~0,003€/1K tokens)
   - Expérimentation illimitée pendant le développement
   - Pas de surprise de facturation

2. **Confidentialité et sécurité**
   - Les alertes de sécurité ne quittent **jamais** ta machine
   - Aucune dépendance à des services cloud tiers
   - Conformité RGPD native
   - Critique pour manipuler des vraies alertes sensibles

3. **Latence optimisée**
   - Pas de round-trip réseau
   - Sur Mac M2 : ~1-3 secondes par analyse
   - Important pour traiter des centaines d'alertes/heure

4. **Contrôle total**
   - Pas de rate limiting
   - Choix du modèle (Llama, Mistral, etc.)
   - Customisation des paramètres (température, context window)

5. **Offline-first**
   - Fonctionne sans connexion Internet
   - Résilience face aux pannes cloud
   - Idéal pour environnements isolés (air-gapped)

### Limites connues

| Critère | Ollama local | Claude API |
|---------|--------------|------------|
| **Performance** | Bien (Llama 3.2 8B) | Excellent (Sonnet 4) |
| **Coût** | 0€ | ~10-30€/mois |
| **Raisonnement complexe** | Bon | Supérieur |
| **Vitesse** | 1-3 sec | 0.5-1 sec |
| **Setup** | Configuration requise | Immédiat |

### Quand migrer vers une API cloud ?

✅ **Reste en local si** :
- Tu développes/apprends
- Tu traites des données sensibles
- Budget limité
- Environnement air-gapped

🔄 **Considère l'API si** :
- Tu passes en production à grande échelle
- Tu as besoin de raisonnement très avancé
- Tu veux déléguer l'infrastructure
- Budget disponible (>50€/mois)

### Performances sur Mac M2

Benchmarks réels avec Llama 3.2 (8B) :

```
Analyse d'une alerte simple : ~2 secondes
Analyse d'une alerte complexe : ~4 secondes
Batch de 10 alertes : ~25 secondes
Throughput : ~24 alertes/minute
```

**Conclusion** : Largement suffisant pour un SOC de taille moyenne (< 1000 alertes/jour).

## 📊 Données de test

Le fichier `data/sample_alerts.json` contient 8 alertes simulant une attaque complète inspirée du rapport Anthropic :

1. **Port Scan** (47 ports/sec) → Pattern IA
2. **SSH Brute Force** (156 tentatives/2min) → Pattern IA
3. **Lateral Movement** → Post-exploitation
4. **Data Exfiltration** (2.3 GB) → Objectif atteint
5. **SQL Injection** → Vecteur d'attaque web
6. **Command Execution** (12 cmd/min) → Pattern IA
7. **Anomalous API Activity** (45 req/sec) → Pattern IA
8. **Credential Harvesting** → Persistence

Ces alertes couvrent les principales phases du framework MITRE ATT&CK.

## 📝 Exemple de sortie

```
============================================================
🛡️  SOC AI ASSISTANT - ANALYSEUR D'ALERTES
============================================================

📂 Chargement des alertes depuis data/sample_alerts.json...
✅ 8 alertes chargées avec succès

🔍 Démarrage de l'analyse de 8 alertes...

📊 Analyse de l'alerte 1/8: alert_001
------------------------------------------------------------

✅ ANALYSE:
CRITICITÉ: CRITICAL

TACTIQUE MITRE ATT&CK: 
- T1046 - Network Service Discovery (Reconnaissance)
- T1595 - Active Scanning

INDICATEURS D'ATTAQUE AUTONOME PAR IA: OUI
- Rythme anormal: 47 ports scannés par seconde
- Vitesse surhumaine incompatible avec scan manuel
- Pattern systématique typique d'automatisation IA

RECOMMANDATIONS D'ACTION IMMÉDIATE:
1. Bloquer immédiatement l'IP source au firewall périmétrique
2. Vérifier les logs d'accès pour tentatives d'exploitation
3. Activer l'IPS en mode prévention sur ce segment
4. Alerter l'équipe IR pour investigation approfondie
5. Examiner le trafic réseau pour d'autres sources similaires

FAUX POSITIF PROBABLE: NON
Haute confiance - Pattern d'attaque confirmé

============================================================

💾 Résultats sauvegardés dans logs/analysis_results.json

============================================================
📈 STATISTIQUES
============================================================
Total alertes analysées: 8
  - high: 3
  - critical: 4
  - medium: 1
============================================================
```

## 🎓 Progression du développement

### ✅ Étapes complétées

**Semaine 1 : Fondations**
- [x] Setup environnement Ollama + Llama 3.2
- [x] Compréhension de l'architecture SOC
- [x] Premiers tests d'interaction avec API LLM
- [x] Construction de prompts structurés
- [x] Fonction `build_prompt()` avec contexte MITRE ATT&CK
- [x] Fonction `send_to_ollama()` avec gestion d'erreurs basique
- [x] Tests sur alerte unique

**Semaine 2 : Analyse batch et orchestration**
- [x] Fonction `build_prompt()` adaptative avec `.get()`
- [x] Support multi-structure (alert_type vs type)
- [x] Fonction `load_alerts_from_file()` avec gestion d'erreurs
- [x] Fonction `analyze_batch()` avec `enumerate(start=1)`
- [x] Affichage de progression visuel [x/total]
- [x] Fonction `save_results()` avec export JSON horodaté
- [x] Fonction `main()` complète pour orchestration
- [x] Statistiques de synthèse par sévérité
- [x] Gestion robuste des erreurs (FileNotFoundError, JSONDecodeError)
- [x] Tests réussis sur les 8 alertes simulées

**Semaine 3 : Base de données MITRE ATT&CK**
- [x] Création de `mitre_database.py` avec dictionnaire de techniques
- [x] 11 techniques MITRE ATT&CK documentées (Reconnaissance, Credential Access, Lateral Movement, Exfiltration, Execution, Initial Access, C2)
- [x] Fonction `get_technique()` pour récupération par ID
- [x] Fonction `search_by_indicator()` pour recherche par mot-clé
- [x] Fonction `get_techniques_by_tactic()` pour filtrage par tactique
- [x] Fonction `get_high_severity_techniques()` pour techniques critiques
- [x] Fonction `get_database_stats()` pour statistiques
- [x] Script de test standalone (`if __name__ == "__main__"`)

### 🔄 En cours d'amélioration

**Phase actuelle : Intégration base MITRE**
- [ ] Intégrer `mitre_database.py` dans `analyzer.py`
- [ ] Utiliser la base MITRE pour enrichir les prompts
- [ ] Auto-détection des techniques MITRE depuis les alertes
- [ ] Génération automatique de recommandations depuis la base
- [ ] Affiner la détection des patterns IA (scoring quantitatif)
- [ ] Ajouter scoring de confiance (0-100%)
- [ ] Implémenter filtrage par sévérité
- [ ] Ajouter métriques de performance (temps/alerte)

### ⏳ Prochaines étapes

**Court terme (prochaine session)**
- [ ] Export rapport en HTML/Markdown
- [ ] Graphiques de distribution (matplotlib)
- [ ] Détection de corrélation temporelle
- [ ] Mode verbose/quiet configurable
- [ ] Tests unitaires avec pytest

## 🚀 Roadmap détaillée

### Court terme (1-2 semaines)
- [ ] **Intégration base MITRE dans l'analyseur** (priorité haute)
- [ ] Auto-mapping alertes → techniques MITRE via indicateurs
- [ ] Enrichissement automatique des prompts avec données MITRE
- [ ] Scoring de confiance quantitatif
- [ ] Filtrage par criticité/sévérité
- [ ] Export rapport HTML avec styling
- [ ] Métriques de performance détaillées
- [ ] Mode debug pour troubleshooting

### Moyen terme (1 mois)
- [ ] Intégration Suricata (IDS réel)
- [ ] Base de données SQLite pour historique
- [ ] Interface web Flask basique
- [ ] Corrélation temporelle d'alertes
- [ ] API REST pour intégration SIEM

### Long terme (3 mois)
- [ ] Dashboard Grafana temps réel
- [ ] Playbooks Ansible automatisés
- [ ] Machine Learning pour false positive reduction
- [ ] Documentation complète API
- [ ] Conteneurisation Docker complète

## 📖 Journal d'apprentissage

### Session 1 - Fondations (18 Nov 2025)

**Objectifs** : Comprendre l'interaction avec un LLM et construire les bases du système

**Concepts maîtrisés** :
1. **API REST avec Ollama** : Communication via `requests.post()` avec corps JSON
2. **Prompt Engineering** : Structure en 5 parties (Rôle, Contexte, Données, Instructions, Format)
3. **Streaming vs Non-streaming** : Choix du mode non-streaming pour analyses structurées
4. **Gestion d'erreurs** : Try/except pour robustesse du système

**Code développé** :
- `build_prompt(alert)` : Construction de prompts contextualisés pour analyse SOC
- `send_to_ollama(prompt)` : Communication avec l'API locale Ollama
- Tests réussis sur alerte SSH Brute Force simulée

### Session 2 - Orchestration et robustesse (29 Nov 2025)

**Objectifs** : Construire un système complet d'analyse batch avec gestion d'erreurs

**Concepts maîtrisés** :
1. **Méthode `.get()` pour dictionnaires** : Accès sécurisé avec valeurs par défaut
2. **`enumerate(start=1)`** : Compteur lisible dans les boucles
3. **Gestion d'erreurs JSON** : FileNotFoundError, JSONDecodeError
4. **Architecture modulaire** : Séparation des responsabilités (load/analyze/save/main)
5. **Timestamps ISO 8601** : Horodatage standardisé avec `datetime.now().isoformat()`

**Code développé** :
- `build_prompt()` adaptatif : Support multi-structure avec `.get()`
- `load_alerts_from_file()` : Chargement robuste avec gestion d'erreurs
- `analyze_batch()` : Boucle optimisée avec `enumerate()`
- `save_results()` : Export JSON avec métadonnées
- `main()` : Orchestration complète du flux d'analyse

**Problème résolu** :
- **KeyError: 'type'** → Solution : `.get("alert_type", alert.get("type", "Unknown"))`
- Adaptation du script à la structure réelle du JSON
- Correction du chemin : `logs/` → `data/sample_alerts.json`

**Tests réussis** :
- Analyse complète des 8 alertes simulées
- Sauvegarde automatique dans `logs/analysis_results.json`
- Statistiques de synthèse par sévérité

**Apprentissages clés** :
- Toujours utiliser `.get()` pour accéder aux clés de dictionnaires incertaines
- `enumerate()` est plus pythonique que `list.index()`
- Une fonction `main()` claire facilite l'orchestration et les tests
- Les statistiques finales ajoutent de la valeur à l'analyse

**Métriques** :
- Temps moyen par alerte : ~3 secondes
- Throughput : ~20 alertes/minute
- Taux de réussite : 100% (8/8 alertes analysées)

### Session 3 - Base de données MITRE ATT&CK (Date à venir)

**Objectifs** : Créer une base de connaissances structurée pour enrichir l'analyse

**Concepts maîtrisés** :
1. **Structure de données hiérarchique** : Dict de techniques avec attributs multiples
2. **Fonctions utilitaires modulaires** : Recherche, filtrage, statistiques
3. **Documentation inline** : Docstrings pour toutes les fonctions
4. **Test standalone** : Script exécutable pour validation

**Code développé** :
- `MITRE_TECHNIQUES` : Dictionnaire de 11 techniques avec indicateurs et recommandations
- `get_technique()` : Récupération par ID avec gestion d'erreurs
- `search_by_indicator()` : Recherche sémantique par mot-clé
- `get_techniques_by_tactic()` : Filtrage par tactique MITRE
- `get_high_severity_techniques()` : Identification des techniques critiques
- `get_database_stats()` : Métriques de la base de données

**Couverture MITRE** :
- 11 techniques couvrant 7 tactiques principales
- Sévérité moyenne : 8.0/10
- 9 techniques haute sévérité (≥8)
- Indicateurs et recommandations pour chaque technique

**Prochaines étapes** :
- Intégration dans `analyzer.py` pour enrichissement automatique
- Auto-mapping alertes → techniques via matching d'indicateurs
- Génération de recommandations depuis la base au lieu du LLM seul

---

## 📚 Ressources

### Sécurité offensive et défensive
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [Suricata Documentation](https://suricata.io/documentation/)
- [TryHackMe - SOC Level 1](https://tryhackme.com/path/outline/soclevel1)

### IA et LLMs
- [Ollama Documentation](https://github.com/ollama/ollama)
- [Llama 3.2 Model Card](https://ai.meta.com/llama/)
- [Anthropic - Threat Intelligence](https://www.anthropic.com/research)

### Python Best Practices
- [Python Requests Library](https://requests.readthedocs.io/)
- [JSON Handling in Python](https://docs.python.org/3/library/json.html)
- [Python Error Handling](https://docs.python.org/3/tutorial/errors.html)

### Rapport de référence
- [Anthropic - First AI-Orchestrated Cyber Espionage Campaign (Nov 2025)](https://www.anthropic.com/research)

## 🤝 Contribution

Ce projet est open-source et éducatif. Les contributions sont les bienvenues :
- 🐛 Signaler des bugs
- 💡 Proposer des améliorations
- 📖 Améliorer la documentation
- 🔧 Soumettre des PR

## ⚖️ Licence

MIT License - Utilisation libre à des fins éducatives et de recherche en sécurité.

**⚠️ Avertissement** : Ce projet est destiné uniquement à des fins éducatives et de recherche en cybersécurité défensive. L'utilisation de ces techniques à des fins malveillantes est illégale.

## 📧 Contact

Pour questions ou suggestions : Ouvrir une issue sur GitHub

---

**Version** : 1.1.0-MVP (stable)  
**Dernière mise à jour** : 29 Novembre 2025  
**Statut** : 🟢 Phase 1 complétée à 95% - Système d'analyse batch fonctionnel  
**Prochaine session** : Optimisation des analyses et scoring de confiance