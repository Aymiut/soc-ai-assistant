# ============================================
# MITRE ATT&CK Database
# ============================================
# Base de connaissance des techniques d'attaque
# Structure : Dict[technique_id] -> Dict[attributs]
# ============================================

MITRE_TECHNIQUES = {
    # ===== RECONNAISSANCE =====
    
    "T1046": {
        "name": "Network Service Discovery",
        "tactic": "Discovery",
        "description": "Scan de ports et services réseau pour identifier les cibles potentielles",
        "severity": 7,
        "sub_techniques": [],
        "indicators": [
            "port scan",
            "service scan",
            "network scanning",
            "ports/sec",
            "nmap",
            "masscan"
        ],
        "recommendations": [
            "Bloquer l'IP source au firewall périmétrique",
            "Activer l'IPS en mode prévention",
            "Limiter la surface d'attaque (fermer ports inutiles)",
            "Configurer rate limiting sur le firewall",
            "Examiner logs pour tentatives d'exploitation"
        ]
    },
    
    "T1595": {
        "name": "Active Scanning",
        "tactic": "Reconnaissance",
        "description": "Reconnaissance active des infrastructures cibles via scanning",
        "severity": 6,
        "sub_techniques": ["T1595.001", "T1595.002"],
        "indicators": [
            "scanning activity",
            "reconnaissance",
            "enumeration",
            "probing"
        ],
        "recommendations": [
            "Identifier et bloquer les sources de scan",
            "Déployer honeypots pour détecter reconnaissance",
            "Monitorer patterns de scanning distribué"
        ]
    },
    
    # ===== CREDENTIAL ACCESS =====
    
    "T1110": {
        "name": "Brute Force",
        "tactic": "Credential Access",
        "description": "Tentatives multiples de connexion pour deviner des credentials",
        "severity": 9,
        "sub_techniques": [
            "T1110.001",  # Password Guessing
            "T1110.002",  # Password Cracking
            "T1110.003",  # Password Spraying
            "T1110.004"   # Credential Stuffing
        ],
        "indicators": [
            "brute force",
            "multiple failed",
            "failed login",
            "authentication failure",
            "failed attempts",
            "rapid attempts",
            "login attempts"
        ],
        "recommendations": [
            "Bloquer immédiatement l'IP source au firewall",
            "Implémenter fail2ban ou équivalent",
            "Vérifier les logs pour tentatives réussies",
            "Activer l'authentification multi-facteurs (MFA)",
            "Configurer account lockout policy",
            "Alerter l'équipe IR si connexion réussie détectée"
        ]
    },
    
    "T1078": {
        "name": "Valid Accounts",
        "tactic": "Credential Access",
        "description": "Utilisation de comptes légitimes compromis",
        "severity": 8,
        "sub_techniques": ["T1078.001", "T1078.002", "T1078.003", "T1078.004"],
        "indicators": [
            "compromised account",
            "stolen credentials",
            "valid account",
            "legitimate credentials"
        ],
        "recommendations": [
            "Révoquer immédiatement les credentials compromis",
            "Forcer réinitialisation de mot de passe",
            "Auditer tous les accès récents du compte",
            "Implémenter MFA sur tous les comptes"
        ]
    },
    
    "T1555": {
        "name": "Credentials from Password Stores",
        "tactic": "Credential Access",
        "description": "Extraction de credentials depuis des gestionnaires de mots de passe",
        "severity": 8,
        "sub_techniques": ["T1555.001", "T1555.002", "T1555.003"],
        "indicators": [
            "credential harvesting",
            "password dump",
            "credential extraction",
            "keychain access"
        ],
        "recommendations": [
            "Chiffrer tous les password stores",
            "Monitorer accès aux credential managers",
            "Implémenter protection contre credential dumping"
        ]
    },
    
    # ===== LATERAL MOVEMENT =====
    
    "T1021": {
        "name": "Remote Services",
        "tactic": "Lateral Movement",
        "description": "Utilisation de services distants pour se déplacer dans le réseau",
        "severity": 8,
        "sub_techniques": ["T1021.001", "T1021.002", "T1021.004", "T1021.006"],
        "indicators": [
            "lateral movement",
            "remote access",
            "internal movement",
            "rdp",
            "ssh lateral",
            "smb connection"
        ],
        "recommendations": [
            "Segmenter le réseau (VLAN, micro-segmentation)",
            "Implémenter Zero Trust architecture",
            "Monitorer connexions inter-segments",
            "Désactiver services distants non nécessaires",
            "Auditer les accès privilégiés"
        ]
    },
    
    # ===== EXFILTRATION =====
    
    "T1041": {
        "name": "Exfiltration Over C2 Channel",
        "tactic": "Exfiltration",
        "description": "Exfiltration de données via le canal de commande et contrôle",
        "severity": 10,
        "sub_techniques": [],
        "indicators": [
            "data exfiltration",
            "large transfer",
            "unusual outbound",
            "suspicious upload",
            "GB transferred"
        ],
        "recommendations": [
            "Bloquer immédiatement le canal C2",
            "Isoler le système compromis du réseau",
            "Identifier données exfiltrées",
            "Lancer investigation forensique complète",
            "Notifier équipe légale et CISO",
            "Implémenter DLP (Data Loss Prevention)"
        ]
    },
    
    "T1048": {
        "name": "Exfiltration Over Alternative Protocol",
        "tactic": "Exfiltration",
        "description": "Exfiltration via protocoles alternatifs (DNS, ICMP, etc.)",
        "severity": 9,
        "sub_techniques": ["T1048.001", "T1048.002", "T1048.003"],
        "indicators": [
            "dns tunneling",
            "icmp exfiltration",
            "alternative protocol",
            "covert channel"
        ],
        "recommendations": [
            "Monitorer trafic DNS/ICMP anormal",
            "Bloquer protocoles non-business critical",
            "Implémenter inspection deep packet"
        ]
    },
    
    # ===== EXECUTION =====
    
    "T1059": {
        "name": "Command and Scripting Interpreter",
        "tactic": "Execution",
        "description": "Exécution de commandes système ou scripts malveillants",
        "severity": 8,
        "sub_techniques": ["T1059.001", "T1059.003", "T1059.004"],
        "indicators": [
            "command execution",
            "shell execution",
            "script execution",
            "powershell",
            "bash",
            "cmd.exe",
            "commands/min"
        ],
        "recommendations": [
            "Bloquer ou surveiller l'exécution de scripts",
            "Implémenter application whitelisting",
            "Monitorer processus parents suspects",
            "Activer logging PowerShell/bash détaillé",
            "Restreindre privilèges d'exécution"
        ]
    },
    
    # ===== INITIAL ACCESS =====
    
    "T1190": {
        "name": "Exploit Public-Facing Application",
        "tactic": "Initial Access",
        "description": "Exploitation de vulnérabilités dans applications web exposées",
        "severity": 9,
        "sub_techniques": [],
        "indicators": [
            "sql injection",
            "web exploit",
            "application vulnerability",
            "injection attack",
            "rce",
            "remote code execution"
        ],
        "recommendations": [
            "Patcher immédiatement la vulnérabilité",
            "Déployer WAF (Web Application Firewall)",
            "Effectuer audit de sécurité applicatif",
            "Implémenter input validation",
            "Isoler l'application compromise"
        ]
    },
    
    # ===== COMMAND AND CONTROL =====
    
    "T1071": {
        "name": "Application Layer Protocol",
        "tactic": "Command and Control",
        "description": "Utilisation de protocoles applicatifs pour C2 (HTTP, DNS, etc.)",
        "severity": 8,
        "sub_techniques": ["T1071.001", "T1071.002", "T1071.003", "T1071.004"],
        "indicators": [
            "anomalous api",
            "suspicious api activity",
            "c2 communication",
            "beaconing",
            "unusual http pattern",
            "req/sec"
        ],
        "recommendations": [
            "Bloquer domaines/IPs C2 identifiés",
            "Analyser trafic pour beaconing patterns",
            "Implémenter proxy avec inspection SSL",
            "Monitorer connexions sortantes suspectes",
            "Isoler systèmes compromis"
        ]
    }
}


# ============================================
# Fonctions utilitaires
# ============================================

def get_technique(technique_id: str) -> dict:
    """
    Récupère une technique MITRE par son ID
    
    Args:
        technique_id: ID de la technique (ex: "T1110")
    
    Returns:
        Dict avec les infos de la technique, ou dict vide si non trouvée
    """
    return MITRE_TECHNIQUES.get(technique_id, {})


def search_by_indicator(keyword: str) -> list:
    """
    Recherche les techniques MITRE par mot-clé dans les indicateurs
    
    Args:
        keyword: Mot-clé à rechercher (ex: "brute force")
    
    Returns:
        Liste des IDs de techniques correspondantes
    """
    keyword_lower = keyword.lower()
    matching_techniques = []
    
    for tech_id, tech_data in MITRE_TECHNIQUES.items():
        # Cherche dans les indicateurs
        for indicator in tech_data.get("indicators", []):
            if keyword_lower in indicator.lower():
                matching_techniques.append(tech_id)
                break  # Une seule correspondance suffit
    
    return matching_techniques

def search_by_multiple_indicators(keywords: list) -> list:
    """
    Recherche les techniques MITRE par plusieurs mots-clés
    
    Args:
        keywords: Liste de mots-clés à rechercher
    
    Returns:
        Liste unique des IDs de techniques correspondantes
    """
    all_matches = set()  # Set pour éviter les doublons automatiquement
    
    for keyword in keywords:
        matches = search_by_indicator(keyword)  # Réutilise la fonction existante
        all_matches.update(matches)  # Ajoute au set
    
    return list(all_matches)


def get_techniques_by_tactic(tactic: str) -> list:
    """
    Filtre les techniques par tactique MITRE
    
    Args:
        tactic: Nom de la tactique (ex: "Credential Access")
    
    Returns:
        Liste des IDs de techniques pour cette tactique
    """
    return [
        tech_id for tech_id, tech_data in MITRE_TECHNIQUES.items()
        if tech_data.get("tactic", "").lower() == tactic.lower()
    ]


def get_high_severity_techniques(threshold: int = 8) -> list:
    """
    Récupère les techniques de haute sévérité
    
    Args:
        threshold: Seuil de sévérité (1-10)
    
    Returns:
        Liste des IDs de techniques >= threshold
    """
    return [
        tech_id for tech_id, tech_data in MITRE_TECHNIQUES.items()
        if tech_data.get("severity", 0) >= threshold
    ]


# ============================================
# Statistiques de la base
# ============================================

def get_database_stats() -> dict:
    """
    Statistiques sur la base de données MITRE
    
    Returns:
        Dict avec nombre de techniques, tactiques, etc.
    """
    tactics = set(tech["tactic"] for tech in MITRE_TECHNIQUES.values())
    avg_severity = sum(tech["severity"] for tech in MITRE_TECHNIQUES.values()) / len(MITRE_TECHNIQUES)
    
    return {
        "total_techniques": len(MITRE_TECHNIQUES),
        "unique_tactics": len(tactics),
        "tactics_list": sorted(tactics),
        "average_severity": round(avg_severity, 2),
        "high_severity_count": len(get_high_severity_techniques())
    }


# ============================================
# Test de la base (si lancé directement)
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("🛡️  MITRE ATT&CK Database - Tests")
    print("=" * 60)
    
    # Stats générales
    stats = get_database_stats()
    print(f"\n📊 Statistiques:")
    print(f"  - Techniques: {stats['total_techniques']}")
    print(f"  - Tactiques uniques: {stats['unique_tactics']}")
    print(f"  - Sévérité moyenne: {stats['average_severity']}/10")
    print(f"  - Haute sévérité (≥8): {stats['high_severity_count']}")
    
    # Test recherche par ID
    print(f"\n🔍 Test: get_technique('T1110')")
    tech = get_technique("T1110")
    print(f"  - Nom: {tech.get('name')}")
    print(f"  - Tactique: {tech.get('tactic')}")
    print(f"  - Sévérité: {tech.get('severity')}/10")
    
    # Test recherche par indicateur
    print(f"\n🔍 Test: search_by_indicator('brute force')")
    results = search_by_indicator("brute force")
    print(f"  - Techniques trouvées: {results}")
    
    # Test filtrage par tactique
    print(f"\n🔍 Test: get_techniques_by_tactic('Credential Access')")
    cred_techs = get_techniques_by_tactic("Credential Access")
    print(f"  - Techniques: {cred_techs}")
    
    print("\n" + "=" * 60)