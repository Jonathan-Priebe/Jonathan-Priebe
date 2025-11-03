# 📖 Automatische README-Updates - Anleitung

## 🎯 Was macht dieses System?

Dieses Setup aktualisiert automatisch den "Currently Working On" Abschnitt in deiner README mit einem Ausschnitt aus der README des verlinkten Projekts.

## 🚀 Installation

### 1. Dateien in dein Repository kopieren

Kopiere diese Dateien in dein Haupt-Repository (z.B. `jonathan-priebe/jonathan-priebe`):

```
.github/
├── workflows/
│   └── update-readme.yml
└── scripts/
    └── update_readme.py
```

### 2. README anpassen

Deine README muss die Marker `<!-- PROJECT_START -->` und `<!-- PROJECT_END -->` enthalten:

```markdown
## 🚀 Currently Working On

<!-- PROJECT_START -->

### 🎮 Projektname

> Hier kommt automatisch die Beschreibung

📁 [View Repository](https://github.com/dein-username/dein-projekt)

<!-- PROJECT_END -->
```

## 🔄 Verwendung

### Automatische Updates

Die README wird automatisch aktualisiert:
- **Täglich** um 00:00 UTC
- Bei jedem **Push** zur `main` Branch
- **Manuell** über GitHub Actions (siehe unten)

### Projekt wechseln - So einfach geht's! ✨

**Du musst nur den Link ändern!** Alles andere passiert automatisch.

1. Öffne deine `README.md`
2. Finde den Abschnitt zwischen `<!-- PROJECT_START -->` und `<!-- PROJECT_END -->`
3. Ändere nur die URL beim Repository-Link:

```markdown
<!-- PROJECT_START -->

### 🎮 alter-projektname  ← wird automatisch aktualisiert

> Alte Beschreibung  ← wird automatisch aktualisiert

📁 [View Repository](https://github.com/jonathan-priebe/NEUES-PROJEKT)  ← NUR DAS ÄNDERN!

<!-- PROJECT_END -->
```

4. Commit und push die Änderung
5. Der GitHub Actions Workflow läuft automatisch und aktualisiert:
   - Den Projektnamen
   - Die Beschreibung (erste 4 Zeilen aus der neuen README)
   - Alles andere bleibt gleich!

### Manuelles Auslösen

Falls du die README sofort aktualisieren möchtest:

1. Gehe zu deinem Repository auf GitHub
2. Klicke auf **Actions**
3. Wähle **Update README with Project Info**
4. Klicke auf **Run workflow**
5. Wähle die Branch (normalerweise `main`)
6. Klicke auf **Run workflow**

## ⚙️ Anpassungen

### Länge der Beschreibung ändern

In der Datei `.github/scripts/update_readme.py`, Zeile 71:

```python
excerpt = get_readme_excerpt(repo_url, max_lines=4)  # Ändere die Zahl
```

### Update-Zeitplan ändern

In der Datei `.github/workflows/update-readme.yml`:

```yaml
schedule:
  - cron: '0 0 * * *'  # Täglich um 00:00 UTC
  # Beispiele:
  # - cron: '0 */6 * * *'  # Alle 6 Stunden
  # - cron: '0 0 * * 1'    # Jeden Montag
```

## 🎨 Emoji für verschiedene Projekttypen

Du kannst das Emoji manuell in der README ändern, wenn du möchtest:

```markdown
### 🐳 Docker Project
### 🎮 Gaming Project
### 🔒 Security Project
### 🤖 Automation Project
### 📱 Mobile App
### 🌐 Web Application
```

Das Emoji wird bei automatischen Updates NICHT überschrieben, nur der Projektname und die Beschreibung!

## 🐛 Troubleshooting

### Workflow läuft nicht

- Prüfe, ob GitHub Actions in deinem Repository aktiviert sind
- Gehe zu **Settings** → **Actions** → **General** → Stelle sicher, dass Actions erlaubt sind

### README wird nicht aktualisiert

- Prüfe die Logs in **Actions**
- Stelle sicher, dass die Marker `<!-- PROJECT_START -->` und `<!-- PROJECT_END -->` korrekt sind
- Prüfe, ob die Repository-URL korrekt formatiert ist

### "Could not parse repository URL"

Die URL muss dieses Format haben:
```
https://github.com/username/repository-name
```

## 📝 Beispiel

**Vorher (manuell gesetzt):**
```markdown
<!-- PROJECT_START -->

### 🐳 conduit-container-setup

> Alte manuelle Beschreibung

📁 [View Repository](https://github.com/jonathan-priebe/pkmn-wfc-server-docker-setup)

<!-- PROJECT_END -->
```

**Nachher (automatisch aktualisiert):**
```markdown
<!-- PROJECT_START -->

### 🎮 pkmn-wfc-server-docker-setup

> Docker-based setup for running a Pokémon Wi-Fi Connection (WFC) server...

📁 [View Repository](https://github.com/jonathan-priebe/pkmn-wfc-server-docker-setup)

<!-- PROJECT_END -->
```

## 💡 Tipps

1. **Schreibe gute README-Dateien** in deinen Projekten - die ersten Zeilen werden automatisch übernommen
2. **Nutze aussagekräftige erste Sätze** in deinen Projekt-READMEs
3. **Der Titel wird automatisch entfernt** - nur der Inhalt wird übernommen
4. **Leere Zeilen am Anfang** werden übersprungen

## 🎉 Fertig!

Jetzt musst du nur noch den Link in deiner README ändern, und alles andere wird automatisch aktualisiert!
