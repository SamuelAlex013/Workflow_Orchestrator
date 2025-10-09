# 🤖 Famulor for n8n

<div align="center">

![Famulor Logo](https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png)

**The most powerful AI calling automation for n8n workflows**

[![npm version](https://badge.fury.io/js/n8n-nodes-famulor.svg)](https://www.npmjs.com/package/n8n-nodes-famulor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English](#english) • [Deutsch](#deutsch) • [Installation](#installation) • [Documentation](https://docs.famulor.de/)

---

</div>

## English

**Transform your n8n workflows with AI-powered phone calls**

This official n8n community node integrates [Famulor](https://www.famulor.io/)'s cutting-edge AI calling platform directly into your automation workflows. Make intelligent phone calls, receive real-time call data, and automate complex communication processes with ease.

### Why Famulor?

🎯 **AI-Powered Conversations** - Deploy intelligent virtual assistants that conduct natural phone conversations  
📊 **Real-time Analytics** - Get instant call results, transcripts, and extracted data  
🔄 **Seamless Integration** - Native n8n integration with no complex setup required  
📱 **Global Reach** - Make calls worldwide with enterprise-grade reliability  

---

## Deutsch

**Verwandeln Sie Ihre n8n-Workflows mit KI-gestützten Telefonanrufen**

Dieser offizielle n8n-Community-Node integriert [Famulors](https://www.famulor.de/) hochmoderne KI-Anrufplattform direkt in Ihre Automatisierungs-Workflows. Führen Sie intelligente Telefonanrufe durch, erhalten Sie Echtzeit-Anrufdaten und automatisieren Sie komplexe Kommunikationsprozesse mit Leichtigkeit.

### Warum Famulor?

🎯 **KI-gestützte Gespräche** - Setzen Sie intelligente virtuelle Assistenten ein, die natürliche Telefongespräche führen  
📊 **Echtzeit-Analytik** - Erhalten Sie sofortige Anrufergebnisse, Transkripte und extrahierte Daten  
🔄 **Nahtlose Integration** - Native n8n-Integration ohne komplexe Einrichtung  
📱 **Globale Reichweite** - Führen Sie weltweit Anrufe mit Enterprise-Level-Zuverlässigkeit durch  

---

## Installation

### English
Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

### Deutsch
Befolgen Sie die [Installationsanleitung](https://docs.n8n.io/integrations/community-nodes/installation/) in der n8n Community Nodes Dokumentation.

---

## Operations / Operationen

### English

**Unified Node Interface** - One node, all capabilities

When you add the **Famulor** node to your workflow, choose between:

#### 🚀 Actions (Regular Node)
**📞 Call Operations**
- **Make Call**: Initiate AI-powered phone conversations
  - Select from your outbound assistants
  - Specify target phone numbers  
  - Add custom variables for personalized conversations
  - Get instant call results and data

**🤖 Assistant Management**  
- **Get Assistants**: Retrieve all your AI assistants
  - Fetch complete assistant configurations
  - Access assistant details (name, ID, status, capabilities)
  - Use in any workflow for dynamic assistant selection

#### ⚡ Triggers (Webhook Node)
**📋 Call Monitoring**
- **Call Ended**: Real-time call completion notifications
  - Monitor specific assistants for call events
  - Receive comprehensive call data:
    - Full conversation transcripts
    - AI-extracted variables and insights
    - Call duration, status, and recordings
    - Lead and campaign information
    - Input/output variable mappings

### Deutsch

**Einheitliche Node-Oberfläche** - Ein Node, alle Funktionen

Wenn Sie den **Famulor**-Node zu Ihrem Workflow hinzufügen, wählen Sie zwischen:

#### 🚀 Aktionen (Regulärer Node)
**📞 Anruf-Operationen**
- **Anruf tätigen**: KI-gestützte Telefongespräche initiieren
  - Auswahl aus Ihren ausgehenden Assistenten
  - Zieltelefonnummern angeben
  - Benutzerdefinierte Variablen für personalisierte Gespräche hinzufügen
  - Sofortige Anrufergebnisse und Daten erhalten

**🤖 Assistenten-Verwaltung**
- **Assistenten abrufen**: Alle Ihre KI-Assistenten abrufen
  - Vollständige Assistenten-Konfigurationen laden
  - Zugriff auf Assistenten-Details (Name, ID, Status, Fähigkeiten)
  - Verwendung in jedem Workflow für dynamische Assistenten-Auswahl

#### ⚡ Trigger (Webhook-Node)
**📋 Anruf-Überwachung**
- **Anruf beendet**: Echtzeit-Benachrichtigungen bei Anrufabschluss
  - Überwachung spezifischer Assistenten für Anruf-Events
  - Umfassende Anrufdaten erhalten:
    - Vollständige Gesprächstranskripte
    - KI-extrahierte Variablen und Erkenntnisse
    - Anrufdauer, Status und Aufzeichnungen
    - Lead- und Kampagnen-Informationen
    - Input/Output-Variablen-Zuordnungen

---

## Credentials / Anmeldedaten

### English

**Quick Setup in 3 Steps**

1. **Get Your API Key**
   - Sign up at [Famulor](https://app.famulor.de/) (German) or [Famulor.io](https://www.famulor.io/) (English)
   - Navigate to your account settings
   - Generate a new API key

2. **Configure n8n**
   - Create new credentials of type "Famulor API"
   - Enter your API key
   - Credentials are automatically validated upon save

3. **Start Automating**
   - Your Famulor account is now connected
   - All assistants and settings sync automatically

### Deutsch

**Schnelle Einrichtung in 3 Schritten**

1. **API-Schlüssel erhalten**
   - Registrieren Sie sich bei [Famulor](https://app.famulor.de/) (Deutsch) oder [Famulor.io](https://www.famulor.io/) (Englisch)
   - Gehen Sie zu Ihren Kontoeinstellungen
   - Generieren Sie einen neuen API-Schlüssel

2. **n8n konfigurieren**
   - Erstellen Sie neue Anmeldedaten vom Typ "Famulor API"
   - Geben Sie Ihren API-Schlüssel ein
   - Anmeldedaten werden beim Speichern automatisch validiert

3. **Automatisierung starten**
   - Ihr Famulor-Konto ist jetzt verbunden
   - Alle Assistenten und Einstellungen synchronisieren automatisch

---

## Compatibility / Kompatibilität

### English
- **Minimum n8n version**: 0.36.1
- **Tested with**: n8n 1.0.0+
- **Platform support**: All n8n deployment types

### Deutsch
- **Minimale n8n-Version**: 0.36.1
- **Getestet mit**: n8n 1.0.0+
- **Plattform-Unterstützung**: Alle n8n-Deployment-Typen

---

## Usage / Verwendung

### English

#### 🎯 Getting Started

1. **Add the Famulor Node** to your workflow
2. **Choose your mode**: Action (for outbound operations) or Trigger (for receiving data)
3. **Configure credentials** using your Famulor API key
4. **Start automating** your phone operations

#### 📞 Making Phone Calls (Actions)

**Quick Setup:**
1. Select **Action** → **Call** → **Make**
2. Choose your **outbound assistant** (loaded from your account)
3. Enter the **target phone number**
4. Add **custom variables** for personalized conversations:
   ```
   customer_name: "John Smith"
   order_id: "12345"
   appointment_time: "3 PM"
   ```
5. **Execute** and receive instant results

#### 🤖 Managing Assistants (Actions)

**Retrieve All Assistants:**
1. Select **Action** → **Assistant** → **Get Assistants**
2. Fetches all assistants with complete configuration data
3. Use for dynamic assistant selection in complex workflows

#### ⚡ Real-time Call Monitoring (Triggers)

**Setup Webhook Triggers:**
1. Select **Trigger** → **Call** → **Call Ended**
2. Choose which **assistant to monitor**
3. Copy the **generated webhook URL**
4. **Important**: Add this URL to your assistant settings in Famulor dashboard
5. Enable webhook notifications in your assistant configuration

**Data You Receive:**
- 📋 Complete call transcripts and recordings
- 📊 AI-extracted variables and insights
- ⏱️ Call duration, timestamps, and status
- 📱 Phone numbers and participant details
- 🎯 Campaign and lead information (if applicable)

### Deutsch

#### 🎯 Erste Schritte

1. **Famulor-Node hinzufügen** zu Ihrem Workflow
2. **Modus wählen**: Aktion (für ausgehende Operationen) oder Trigger (für Datenempfang)
3. **Anmeldedaten konfigurieren** mit Ihrem Famulor-API-Schlüssel
4. **Automatisierung starten** Ihrer Telefon-Operationen

#### 📞 Telefonanrufe tätigen (Aktionen)

**Schnelle Einrichtung:**
1. Wählen Sie **Aktion** → **Call** → **Make**
2. Wählen Sie Ihren **ausgehenden Assistenten** (aus Ihrem Konto geladen)
3. Geben Sie die **Zieltelefonnummer** ein
4. Fügen Sie **benutzerdefinierte Variablen** für personalisierte Gespräche hinzu:
   ```
   kundenname: "Max Mustermann"
   bestell_id: "12345"
   termin_zeit: "15 Uhr"
   ```
5. **Ausführen** und sofortige Ergebnisse erhalten

#### 🤖 Assistenten verwalten (Aktionen)

**Alle Assistenten abrufen:**
1. Wählen Sie **Aktion** → **Assistant** → **Get Assistants**
2. Lädt alle Assistenten mit vollständigen Konfigurationsdaten
3. Verwenden Sie für dynamische Assistenten-Auswahl in komplexen Workflows

#### ⚡ Echtzeit-Anrufüberwachung (Trigger)

**Webhook-Trigger einrichten:**
1. Wählen Sie **Trigger** → **Call** → **Call Ended**
2. Wählen Sie, welchen **Assistenten Sie überwachen** möchten
3. Kopieren Sie die **generierte Webhook-URL**
4. **Wichtig**: Fügen Sie diese URL in Ihre Assistenten-Einstellungen im Famulor-Dashboard hinzu
5. Aktivieren Sie Webhook-Benachrichtigungen in Ihrer Assistenten-Konfiguration

**Erhaltene Daten:**
- 📋 Vollständige Anruftranskripte und Aufzeichnungen
- 📊 KI-extrahierte Variablen und Erkenntnisse
- ⏱️ Anrufdauer, Zeitstempel und Status
- 📱 Telefonnummern und Teilnehmerdetails
- 🎯 Kampagnen- und Lead-Informationen (falls zutreffend)

---

## Resources / Ressourcen

### English

📚 **Documentation & Guides**
- [Famulor Documentation](https://docs.famulor.de/) - Complete platform documentation  
- [Famulor API Reference](https://docs.famulor.de/api-reference/) - Technical API documentation
- [n8n Community Nodes Guide](https://docs.n8n.io/integrations/#community-nodes) - n8n integration docs

🌐 **Platforms & Support**
- [Famulor.io](https://www.famulor.io/) - English platform & signup
- [Famulor.de](https://www.famulor.de/) - German platform & signup  
- [Famulor App](https://app.famulor.de/) - Login to your dashboard

### Deutsch

📚 **Dokumentation & Anleitungen**
- [Famulor-Dokumentation](https://docs.famulor.de/) - Vollständige Plattform-Dokumentation
- [Famulor-API-Referenz](https://docs.famulor.de/api-reference/) - Technische API-Dokumentation  
- [n8n-Community-Nodes-Anleitung](https://docs.n8n.io/integrations/#community-nodes) - n8n-Integrations-Dokumentation

🌐 **Plattformen & Support**
- [Famulor.io](https://www.famulor.io/) - Englische Plattform & Anmeldung
- [Famulor.de](https://www.famulor.de/) - Deutsche Plattform & Anmeldung
- [Famulor App](https://app.famulor.de/) - Anmeldung zu Ihrem Dashboard

---

## About Famulor / Über Famulor

### English

Famulor is the leading AI-powered calling platform that revolutionizes business communications. Our intelligent virtual assistants conduct natural phone conversations, extract meaningful data, and integrate seamlessly into your existing workflows.

**Why Choose Famulor?**
- 🧠 **Advanced AI** - GPT-powered conversations that sound human  
- 🔒 **Enterprise Security** - GDPR-compliant with enterprise-grade encryption
- 🌍 **Global Scale** - Make calls worldwide with local presence
- 📈 **Proven Results** - Trusted by businesses across industries

### Deutsch

Famulor ist die führende KI-gestützte Anrufplattform, die die Geschäftskommunikation revolutioniert. Unsere intelligenten virtuellen Assistenten führen natürliche Telefongespräche, extrahieren aussagekräftige Daten und integrieren sich nahtlos in Ihre bestehenden Workflows.

**Warum Famulor wählen?**
- 🧠 **Fortgeschrittene KI** - GPT-gestützte Gespräche, die menschlich klingen
- 🔒 **Unternehmenssicherheit** - DSGVO-konform mit Enterprise-Level-Verschlüsselung  
- 🌍 **Globale Reichweite** - Weltweite Anrufe mit lokaler Präsenz
- 📈 **Bewährte Ergebnisse** - Vertrauen von Unternehmen aller Branchen

---

<div align="center">

**Ready to automate your phone calls? / Bereit, Ihre Telefonanrufe zu automatisieren?**

[🚀 Get Started with Famulor](https://app.famulor.de/) • [📖 Read the Docs](https://docs.famulor.de/) • [💬 Get Support](https://www.famulor.io/support)

*Built with ❤️ by the Famulor team*

</div>
