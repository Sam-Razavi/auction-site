# Auction Site – Flask Web Application

Detta projekt är en enkel auktionswebbplats byggd med **Flask** som en del av kursen  
**Applikationsutveckling för webben**.

Applikationen låter användare se auktioner, söka och filtrera, lägga bud samt interagera med auktioner.  
Administratörer kan logga in och hantera auktioner och bud via ett admin-gränssnitt.

---

## Funktionalitet

### För användare
- Visa alla auktioner
- Se auktion i detalj
- Lägga bud på auktioner
- Visa de högsta buden
- Söka och filtrera auktioner
- Sortera auktioner (t.ex. slutar snart)
- Se auktionens status (kommande / pågående / avslutad)
- Gilla och ogilla auktioner
- Visa bilder kopplade till auktioner

### För administratör
- Logga in via admin-panel
- Skapa nya auktioner
- Redigera befintliga auktioner
- Ta bort auktioner
- Ta bort bud
- Ange bildfil för auktioner

---

## Tekniker

- Python
- Flask
- SQLite
- HTML / CSS
- Jinja2 templates

---


## Installation (lokalt)

1. Klona projektet
```bash
git clone <repo-url>
cd auction-site

2. Skapa och aktivera virtuellt miljö
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

3. Installera beroenden
pip install -r requirements.txt

4. pip install -r requirements.txt
python init_db.py
python seed_db.py

5. Starta applikationen
python run.py





