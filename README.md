# ROADMAP

## GENERAL DIRECTORY STRUCTURE
my_fullstack_project/
├── .env
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py          # App initialization & routing
│   ├── database.py      # DB connection
│   ├── models.py        # SQLAlchemy tables
│   │
│   ├── templates/       # Jinja2 HTML templates live here
│   │   ├── base.html    # Core layout (loads HTMX and CSS)
│   │   ├── index.html   # Main dashboard view
│   │   └── partials/    # Fragment templates swapped dynamically by HTMX
│   │       └── item_row.html
│   │
│   └── static/          # CSS, images, and client-side assets
│       └── styles.css

## STRUCTURE SPECIFICATION
stack: **HTMX + jinja2 stack**
api keys and management: **fastAPI python**
database: **SQLite**



## FRONTEND
