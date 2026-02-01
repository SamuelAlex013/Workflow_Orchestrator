![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# 🕸️ DOM Snapshot Node

**DOM Snapshot** to niestandardowy węzeł dla [n8n](https://n8n.io/), który umożliwia pobranie pełnego kodu HTML strony internetowej za pomocą biblioteki [Playwright](https://playwright.dev/).  
Node otwiera podany adres URL w przeglądarce Chromium w trybie headless, czeka na wskazany moment załadowania strony, a następnie zwraca zrzut DOM w formacie HTML.

---

## ✨ Funkcjonalności

- Otwiera stronę w Playwright Chromium.  
- Czeka na wybrane zdarzenie załadowania strony:
  - **Load** – pełne załadowanie strony.  
  - **DOM Content Loaded** – załadowanie drzewa DOM.  
  - **Network Idle** – brak aktywnych połączeń sieciowych.  
- Zwraca zawartość strony (`<html>...</html>`) w polu `data` w JSON.  
- Obsługuje parametr timeout (maksymalny czas oczekiwania).  
- Może działać jako node typu `transform` lub jako narzędzie (usable as tool).  

---

## ⚙️ Parametry

| Nazwa              | Typ       | Domyślna wartość | Opis                                                                 |
|---------------------|-----------|------------------|----------------------------------------------------------------------|
| **URL**            | string    | –                | Adres strony, którą chcesz pobrać. Wymagane.                        |
| **Wait Until**     | options   | `networkidle`    | Moment, w którym uznać stronę za załadowaną (`load`, `domcontentloaded`, `networkidle`). |
| **Timeout (ms)**   | number    | `30000`          | Maksymalny czas (w milisekundach) oczekiwania na załadowanie strony. |

---

## 📦 Instalacja
### 🔹 Przez interfejs GUI n8n
1. Wejdź w ustawienia **Community Nodes** w n8n.  
2. Kliknij **Install** i podaj nazwę repozytorium: n8n-nodes-domsnapshot
3. n8n automatycznie pobierze i zainstaluje paczkę wraz z wymaganymi zależnościami.  
4. Po restarcie n8n node **DOM Snapshot** będzie dostępny w edytorze workflow.

### Manualna
1. Sklonuj repozytorium lub skopiuj kod node’a do swojego katalogu **community nodes** w n8n.  
    ```bash
    git clone https://github.com/poewer/n8n-nodes-domsnapshot
    ```
2. W katalogu node’a uruchom:
    ```bash
    npm install
    ```
3. playwright zostanie zainstalowany automatycznie,

4. a dzięki postinstall zostanie również pobrane Chromium (npx playwright install chromium).

5. Zbuduj node:
    ```bash
    npm run build
    ```


6. Uruchom n8n z włączoną obsługą community nodes i dodaj DOM Snapshot do swojego workflow.


## 🚀 Przykład użycia

1. Dodaj node DOM Snapshot w workflow.

2. Podaj adres URL, np. https://example.com.

3. Ustaw tryb oczekiwania, np. Network Idle.

4. Uruchom workflow.

### Przykładowy output w polu json.data:
  ``` json
  {
    "data": "<!DOCTYPE html><html><head>...</head><body>...</body></html>"
  }
  ```

## 🛠️ Obsługa błędów

- Brak wartości w polu URL powoduje błąd.

- Jeśli strona nie załaduje się w zadanym czasie, zwrócony zostanie błąd.

- Jeśli w n8n włączona jest opcja Continue On Fail, błąd zostanie przypisany do danego elementu (itemIndex), a workflow będzie kontynuowany.

## Licencja

[MIT]()
