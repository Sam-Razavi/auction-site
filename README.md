# Auction Site – Flask Web Application

A simple auction web application built with **Flask**, created as part of the course **Application Development for the Web**.

Users can browse, search, and bid on auctions. Administrators can manage auctions and bids through a dedicated admin panel.

---

## Features

### Users
- Browse all auctions
- View auction details
- Place bids
- See the highest bids
- Search and filter auctions
- Sort auctions (e.g. ending soon)
- View auction status (upcoming / active / ended)
- Like and dislike auctions
- View images associated with auctions

### Administrators
- Log in via the admin panel
- Create new auctions
- Edit existing auctions
- Delete auctions and bids
- Attach images to auctions

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask 3.1 |
| Database | SQLite |
| Templating | Jinja2 |
| Frontend | HTML, CSS |

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repo-url>
cd auction-site
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialise and seed the database

```bash
python init_db.py
python seed_db.py
```

### 5. Start the application

```bash
python run.py
```

The app will be available at **http://127.0.0.1:5000**.

The admin panel is accessible at **http://127.0.0.1:5000/admin**.
