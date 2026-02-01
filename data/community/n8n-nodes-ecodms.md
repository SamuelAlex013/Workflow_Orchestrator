# n8n-nodes-ecodms

Diese Node ermöglicht die Integration von [ecoDMS](https://www.ecodms.de/) in n8n, um Dokumente automatisiert zu verwalten, zu archivieren und zu klassifizieren.

## Inhaltsverzeichnis
- [Installation](#installation)
- [Funktionen](#funktionen)
- [Konfiguration](#konfiguration)
- [API-Hinweise](#api-hinweise)
- [Nutzung](#nutzung)
- [Nutzung mit dem AI-Agent](#nutzung-mit-dem-ai-agent)
- [Fehlerbehandlung](#fehlerbehandlung)
- [Entwicklung](#entwicklung)
- [Projektstruktur](#projektstruktur)
- [Beitragen](#beitragen)

## Installation

Folgen Sie diesen Schritten, um die Node zu installieren:

```bash
# Globale Installation
npm install -g n8n-nodes-ecodms

# Installation in Ihrer n8n-Installation
cd ~/.n8n/
npm install n8n-nodes-ecodms
```

Bei Docker-basierten Installationen können Sie die Node in einem benutzerdefinierten Container einbinden. Fügen Sie dazu folgende Zeile in Ihr Dockerfile hinzu:

```dockerfile
RUN cd /usr/local/lib/node_modules/n8n && npm install n8n-nodes-ecodms
```

## Funktionen

Diese Node unterstützt folgende Funktionen:

- **Dokumente**: 
  - Dokumente herunterladen und hochladen
  - Spezifische Klassifikationen und Versionen von Dokumenten abrufen
  - Dokument-Versionen herunterladen
  - Klassifikationen erstellen und aktualisieren
  - Dokument-Verknüpfungen hinzufügen und entfernen
  - Versionen zu bestehenden Dokumenten hinzufügen
  - Duplikate prüfen
  - Template-Erkennung für Dokumente
- **Archive**: 
  - Verfügbare Archive auflisten und verbinden
  - Archiv-Informationen abrufen
- **Suche**: 
  - Einfache und erweiterte Dokumentsuche
  - Komplexe Suchfilter mit mehreren Kriterien
  - Sortierung und Filterung von Suchergebnissen
  - Kombinierte Suche mit Dokumenten-Download
- **Ordner**: 
  - Komplette Ordnerstruktur abrufen
  - Ordner und Unterordner erstellen
  - Ordner-Attribute bearbeiten
  - Berechtigungen für Ordner festlegen
- **Klassifikation**:
  - Klassifikationsattribute abrufen (normal und detailliert)
  - Dokumenttyp-Klassifikationen abrufen
  - Dokumente klassifizieren und Klassifikationen aktualisieren
- **Dokumenttypen**:
  - Liste aller verfügbaren Dokumenttypen abrufen
  - Dokumenttyp-Details wie IDs und Namen für die Suche verwenden
- **Thumbnails**: 
  - Vorschaubilder von Dokumenten herunterladen
  - Miniaturansichten für die Anzeige in Oberflächen generieren
- **Lizenzinformationen**: 
  - Informationen zur ecoDMS-Lizenz abrufen
  - Verfügbare API-Connects einsehen
- **Workflow**:
  - Kombinierte Operationen für häufige Anwendungsfälle
  - Optimierte Abläufe für Standard-Szenarien

## Konfiguration

Um die ecoDMS-Node zu verwenden, benötigen Sie:

1. Die URL Ihres ecoDMS-Servers (mit Port, z.B. http://ecodms.example.com:8080)
2. Einen gültigen Benutzernamen und Passwort mit API-Zugriff
3. Die entsprechenden Berechtigungen im ecoDMS-System:
   - Rolle `ecoSIMSCLASSIFY` für Klassifikationen
   - Lese- und/oder Schreibberechtigungen für die entsprechenden Dokumente

Für die Einrichtung:
1. Fügen Sie in n8n unter "Credentials" einen neuen "ecoDMS account" hinzu
2. Geben Sie die Server-URL, Benutzername und Passwort ein
3. Speichern Sie die Anmeldedaten

## API-Hinweise

Die ecoDMS-API verwendet HTTP Basic Authentication und benötigt für bestimmte Funktionen spezielle Accept-Header:

- Standardmäßig werden Antworten im Format `application/json` zurückgegeben
- Für Dokument-Downloads und Thumbnails muss der Accept-Header `*/*` verwendet werden
- Die API unterstützt nur UTF-8-Kodierung

Beachten Sie, dass für die Verwendung der API sogenannte "API connects" benötigt werden:
- 1 API connect = 1 monatlicher Upload oder Download über die ecoDMS API
- Die Anzahl der verfügbaren API connects wird mit dem ersten Upload oder Download in einem neuen Monat zurückgesetzt
- Die verfügbare Anzahl an API connects hängt von Ihrem ecoDMS-Lizenzmodell ab

## Nutzung

Nach der Installation können Sie die ecoDMS-Node in Ihren Workflows verwenden:

1. Ziehen Sie die ecoDMS-Node in Ihren Workflow
2. Wählen Sie die gewünschte Ressource (Dokument, Archiv, Suche, Ordner, etc.)
3. Wählen Sie die entsprechende Operation
4. Konfigurieren Sie die erforderlichen Parameter
5. Verbinden Sie die Node mit anderen Nodes in Ihrem Workflow

Typische Anwendungsfälle:

### Beispiel 1: Dokumente automatisiert archivieren
```
E-Mail-Eingang → E-Mail-Anhänge extrahieren → ecoDMS (Dokument hochladen)
```

### Beispiel 2: Dokumente suchen und verarbeiten
```
ecoDMS (Dokument suchen) → HTTP Request (Daten an externes System senden)
```

### Beispiel 3: Dokumentenklassifikation aktualisieren
```
HTTP Webhook (neues Ereignis) → ecoDMS (Dokument-Klassifikation aktualisieren)
```

## Nutzung mit dem AI-Agent

Diese Node ist vollständig mit dem n8n AI-Agent kompatibel. Folgende Beispielanweisungen können Sie dem AI-Agent geben:

- "Suche nach allen Dokumenten mit dem Stichwort 'Rechnung' im Ordner 'Finanzen'"
- "Lade das Dokument mit der ID 123 herunter und speichere es als PDF"
- "Erstelle einen neuen Ordner für das Jahr 2025"
- "Aktualisiere die Klassifikation des Dokuments mit der ID 456"
- "Zeige mir alle verfügbaren Dokumenttypen im System an"

## Fehlerbehandlung

Die Node beinhaltet umfangreiche Fehlerbehandlung, um typische Probleme zu diagnostizieren:

- **404-Fehler**: Deuten oft auf falsche Dokument- oder Klassifikations-IDs hin
- **401-Fehler**: Probleme mit Authentifizierung oder fehlenden Berechtigungen
- **Fehlgeschlagene API-Aufrufe**: Die Node liefert detaillierte Fehlermeldungen mit konkreten Hinweisen zur Behebung

Sollten Sie auf Probleme stoßen, prüfen Sie:
1. Ob die Server-URL korrekt ist (inkl. Port)
2. Ob die Anmeldedaten gültig sind
3. Ob der Benutzer die notwendigen Berechtigungen hat
4. Ob die angegebenen IDs (Dokument, Klassifikation, Ordner) existieren

## Entwicklung

```bash
# Installation
npm install

# Bauen
npm run build

# Entwicklung mit automatischem Rebuild
npm run dev
```

### Modul-Tests

Das Projekt enthält Tests, die Sie wie folgt ausführen können:

```bash
npm run test
```

## Projektstruktur

Dieses Projekt verwendet eine modulare Struktur, um die Wartbarkeit und Übersichtlichkeit zu verbessern:

```
nodes/EcoDMS/
├── EcoDMS.node.ts         # Hauptdatei, die alle Module zusammenführt
├── ecoDms.svg             # Icon für die Node
├── handlers/              # Handler für die API-Aufrufe
│   ├── documentHandler.ts # Handler für Dokument-Operationen
│   ├── searchHandler.ts   # Handler für Such-Operationen
│   └── ...                # Weitere Handler
├── resources/
│   ├── document.ts        # Modul für Dokument-Ressource
│   ├── classification.ts  # Modul für Klassifikations-Ressource
│   ├── documentType.ts    # Modul für Dokumenttyp-Ressource
│   ├── archive.ts         # Modul für Archiv-Ressource
│   ├── search.ts          # Modul für Such-Ressource
│   ├── folder.ts          # Modul für Ordner-Ressource
│   ├── license.ts         # Modul für Lizenz-Ressource
│   └── workflow.ts        # Modul für kombinierte Workflows
└── utils/
    ├── constants.ts       # Gemeinsame Konstanten (Resource, Operation)
    └── helpers.ts         # Hilfsfunktionen
```

Diese Struktur bietet folgende Vorteile:
- **Bessere Übersichtlichkeit**: Jede Ressource hat eine eigene Datei
- **Einfachere Wartung**: Änderungen an einer bestimmten Ressource betreffen nur eine Datei
- **Vermeidung von Duplikaten**: Parameter, die mehrfach verwendet werden, können in einer Datei definiert werden
- **Leichteres Hinzufügen neuer Funktionalitäten**: Neue Ressourcen können einfach als neue Module hinzugefügt werden

Um neue Ressourcen hinzuzufügen:
1. Erstelle eine neue Datei unter `resources/`
2. Definiere die Operations und Fields für diese Ressource
3. Erstelle einen Handler unter `handlers/`
4. Importiere die neue Datei in `EcoDMS.node.ts` und füge die Operations und Fields hinzu

## Beitragen

Contributions sind willkommen! Bitte erstellen Sie einen Issue oder Pull Request auf GitHub. 

Bei Fragen oder Problemen können Sie auch einen Issue auf dem GitHub-Repository erstellen: [terschawebIT/n8n-nodes-ecodms](https://github.com/terschawebIT/n8n-nodes-ecodms/issues) 