import requests
import json
from datetime import datetime
import mitre_database

def build_prompt(alert, mitre_techniques=None):
    """Construit un prompt structuré pour l'analyse SOC"""
    # Extraire les données avec des valeurs par défaut
    alert_id = alert.get("id", "Unknown")
    alert_type = alert.get("alert_type", alert.get("type", "Unknown"))
    severity = alert.get("severity", "Unknown")
    source_ip = alert.get("source_ip", "Unknown")
    
    # ⭐ NOUVELLE SECTION : Construction du contexte MITRE dynamique
    if mitre_techniques and len(mitre_techniques) > 0:
        mitre_section = "\nTECHNIQUES MITRE ATT&CK DÉTECTÉES:\n\n"
        for tech in mitre_techniques:
            mitre_section += f"🎯 Technique {tech['id']} - {tech['name']}\n"
            mitre_section += f"   Tactique: {tech['tactic']}\n"
            mitre_section += f"   Sévérité: {tech['severity']}/10\n"
            mitre_section += f"   Description: {tech['description']}\n"
            mitre_section += f"   Recommandations:\n"
            for rec in tech['recommendations']:
                mitre_section += f"      - {rec}\n"
            mitre_section += "\n"
    else:
        # Si aucune technique détectée, contexte générique
        mitre_section = "\nCONTEXTE MITRE ATT&CK:\nUtilise le framework MITRE ATT&CK pour classifier cette attaque.\n"
    
    # Construction du prompt adaptatif
    prompt = f"""Tu es un analyste SOC expert en cybersécurité.

CONTEXTE : Nous surveillons des attaques automatisées par IA qui se caractérisent par des rythmes surhumains d'opérations.

ALERTE À ANALYSER :
- ID : {alert_id}
- Type : {alert_type}
- Sévérité : {severity}
- IP source : {source_ip}

DONNÉES COMPLÈTES :
{json.dumps(alert, indent=2, ensure_ascii=False)}

{mitre_section}

TÂCHE : Analyse cette alerte et fournis :
1. Le niveau de criticité (Low/Medium/High/Critical)
2. Si c'est probablement une attaque par IA (oui/non et pourquoi)
3. La tactique MITRE ATT&CK correspondante (en tenant compte des techniques détectées ci-dessus)
4. Une recommandation d'action immédiate

FORMAT : Réponds de manière concise et structurée."""
    
    return prompt


def send_to_ollama(prompt):
    """Envoie un prompt à l'API Ollama locale"""
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json().get("response", "")
    except requests.exceptions.RequestException as e:
        return f"❌ Erreur API Ollama: {e}"


def load_alerts_from_file(file_path):
    """Charge les alertes depuis un fichier JSON"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            alerts = json.load(f)
        return alerts
    except FileNotFoundError:
        print(f"❌ Fichier introuvable: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Erreur de parsing JSON: {e}")
        return []


def analyze_batch(alerts):
    """Analyse un batch d'alertes"""
    results = []
    
    print(f"\n🔍 Démarrage de l'analyse de {len(alerts)} alertes...\n")
    
    for i, alert in enumerate(alerts, start=1):
        alert_id = alert.get("id", f"alert_{i}")
        print(f"📊 Analyse de l'alerte {i}/{len(alerts)}: {alert_id}")
        print("-" * 60)
        
        mitres_techniques = find_relevant_techniques(alert)
        # Construction du prompt
        prompt = build_prompt(alert,mitre_techniques=mitres_techniques)
        
        # Envoi à Ollama
        response = send_to_ollama(prompt)
        
        # Stockage du résultat
        results.append({
            "alert_id": alert_id,
            "alert_type": alert.get("alert_type", alert.get("type", "Unknown")),
            "severity": alert.get("severity", "Unknown"),
            "mitre_techniques_detected": [tech['id'] for tech in mitres_techniques],
            "response": response,
            "analyzed_at": datetime.now().isoformat()
        })
        
        # Affichage de la réponse
        print(f"\n✅ ANALYSE:\n{response}\n")
        print("=" * 60 + "\n")
    
    return results


def save_results(results, output_file="logs/analysis_results.json"):
    """Sauvegarde les résultats dans un fichier JSON"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"💾 Résultats sauvegardés dans {output_file}")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde: {e}")


def find_relevant_techniques(alert):
    """
    Trouve les techniques MITRE pertinentes pour une alerte
    
    Paramètres:
        alert: dict contenant description, type, etc.
    
    Retourne:
        list de technique_ids correspondants
    """
    description = alert.get("description", "")
    alert_type = alert.get("alert_type", alert.get("type", ""))
    
    text = f"{description} {alert_type}".lower()
    keywords = [word for word in text.split() if len(word) > 3]  # Filtre les petits mots
    
    technique_ids = mitre_database.search_by_multiple_indicators(keywords)
    techniques = []
    for tid in technique_ids:
        techniques.append(mitre_database.get_technique(tid))
    return techniques


def main():
    """Fonction principale d'orchestration"""
    print("=" * 60)
    print("🛡️  SOC AI ASSISTANT - ANALYSEUR D'ALERTES")
    print("=" * 60)
    
    # Chemin du fichier d'alertes (corrigé selon ton README)
    alerts_file = "data/sample_alerts.json"
    
    # Chargement des alertes
    print(f"\n📂 Chargement des alertes depuis {alerts_file}...")
    alerts = load_alerts_from_file(alerts_file)
    
    if not alerts:
        print("❌ Aucune alerte à analyser.")   
        return
    
    print(f"✅ {len(alerts)} alertes chargées avec succès\n")
    
    # Analyse des alertes
    results = analyze_batch(alerts)
    
    # Sauvegarde des résultats
    save_results(results)
    
    # Statistiques finales
    print("\n" + "=" * 60)
    print("📈 STATISTIQUES")
    print("=" * 60)
    print(f"Total alertes analysées: {len(results)}")
    
    # Compte par sévérité
    severity_count = {}
    for result in results:
        sev = result.get("severity", "Unknown")
        severity_count[sev] = severity_count.get(sev, 0) + 1
    
    for severity, count in severity_count.items():
        print(f"  - {severity}: {count}")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
    