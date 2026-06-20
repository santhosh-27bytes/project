# CareerPilot AI — Fixed & Connected

This is the cleaned-up, de-duplicated, and fully wired version of the
"interview system" project (your upload had the entire project nested
inside itself twice — this is the single, correct copy with all
errors fixed).

## What was fixed

**Backend**
- Every route now actually calls its matching service function
  (`career_match`, `roadmap`, `skill_gap`, `interview`, `resume`)
  instead of returning hardcoded fake data.
- `/upload-resume` no longer crashes — it creates the `uploads/`
  folder automatically and returns real extracted skills from the PDF.
- Added the missing `/report/download` route, which generates and
  serves a real PDF report.
- `/login` and `/register` validate required fields.
- Added `backend/requirements.txt`.

**Frontend**
- Fixed the CSS path on every page (`../styling/..` → `styling/..`,
  since the `styling` folder is a sibling of the HTML files, not a
  parent).
- Fixed `login.html`, which pointed at a CSS file that didn't exist
  and was missing the `id` attributes its own JavaScript needed.
- Rewired `login.js`, `register.js`, `career-match.js`, `roadmap.js`,
  `skill-gap.js`, `resume.js`, `interview.js`, and `report.js` to
  actually call the Flask backend (was pointing at the wrong port,
  or commented out, or never sending the file at all).
- Fixed `dashboard.js`, which referenced a button that doesn't exist
  on that page (would crash on load).
- Wired up navigation: the dashboard sidebar and module buttons, and
  the homepage's Login/Register/Get Started buttons, now actually
  take you to the right page instead of doing nothing.

## How to run it

### 1. Backend (Flask API)

```bash
cd backend
pip install -r requirements.txt
python3 app.py
```

This starts the API at `http://localhost:5000`.

### 2. Frontend

Open `frontend/index.html` directly in your browser, or serve it
with a simple static server, e.g.:

```bash
cd frontend
python3 -m http.server 5500
```

Then visit `http://localhost:5500`.

The frontend calls the backend at `http://localhost:5000`, so make
sure the Flask server is running first.

## Note on the database

`database.sql` defines a full MySQL schema, but nothing in the Flask
backend currently connects to a database — all data is in-memory or
hardcoded in the service files. If you want persistent storage
(saved users, resumes, scores), the backend would need a DB
connection layer (e.g. via `mysql-connector-python` or `SQLAlchemy`)
added on top of this. That's a bigger feature addition rather than a
bug fix, so I left it out of scope here — let me know if you'd like
that wired up too.
