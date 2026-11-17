# JobAtlas

Track job applications as an interactive map: **Category → Company → Role → Application → Stages**.
FastAPI + SQLite backend, plain HTML/JS frontend (no npm, no build step).

## Run

From the project root (the folder containing `backend/` and `frontend/`):

```bash
pip install -r backend/requirements.txt   # first time only
python -m backend.sync                    # load the JSON data into the database
uvicorn backend.main:app --reload         # start the app
```

- App: http://127.0.0.1:8000
- API docs: http://127.0.0.1:8000/docs
- Tests: `python -m pytest backend/tests -q`

## Bulk add with JSON

`backend/seed/` has one file per table: `categories`, `companies`, `jobs`, `applications`, `progress` (`.json`).
They always mirror the database: changes made in the app are written back automatically.

```bash
python -m backend.sync          # import new/changed records, then re-export
python -m backend.sync import   # JSON -> database only
python -m backend.sync export   # database -> JSON only
```

- Records are matched by name, not id. A missing field leaves the value unchanged; `null` clears it.
- Sync never deletes. Delete from the app.
- To rename a company or role, use the app (renaming in JSON creates a new record).
- Records with errors are skipped and listed; the JSON files are then left untouched so you can fix them.

```jsonc
// categories.json
[{ "name": "Software", "description": "SWE roles" }]

// companies.json
[{ "name": "Google", "category": "Software", "website": "https://careers.google.com", "location": "Bangalore" }]

// jobs.json   job_type: internship | full_time | part_time | contract | other
[{ "company": "Google", "title": "SWE Intern 2027", "job_type": "internship",
   "job_url": "https://...", "date_discovered": "2026-11-04", "deadline": "2026-11-30" }]

// applications.json
[{ "company": "Google", "job": "SWE Intern 2027", "status": "applied", "priority": "high",
   "applied_date": "2026-11-05", "next_action": "Follow up", "next_action_date": "2026-11-20" }]

// progress.json   result: pending | passed | failed | cancelled
[{ "company": "Google", "job": "SWE Intern 2027", "stage": "Online Assessment",
   "stage_date": "2026-11-12", "result": "passed" }]
```

## Rules

- Statuses: `discovered`, `interested` (not applied) · `applied`, `assessment`, `interviewing`, `offer`, `on_hold` (ongoing) · `accepted`, `rejected`, `withdrawn`, `expired` (closed).
- Company names are unique; a role title is unique within its company; one application per role;
  stage names are unique per application (use "Technical Interview 2" for a second round).
- Deleting anything also deletes everything under it.

## Good to know

- Database: `data/jobatlas.db`. To start fresh, delete it and run `python -m backend.sync`.
- No migrations yet: after changing the database tables, delete the `.db` file and re-sync from JSON.
- `backend/seed/*.json` holds your personal data; add it to `.gitignore` if the repo is public.
- Optional settings in a `.env` file in the project root: `DATABASE_URL`, `AUTO_EXPORT_JSON=false`, `CORS_ORIGINS`.

## Project layout

```text
backend/
  main.py          app entry (serves API + frontend)
  sync.py          JSON <-> database sync
  seed/            JSON data files
  api/routes/      endpoints        services/   business logic, graph, stats
  repositories/    DB queries       models/     tables      schemas/  request/response
  core/            settings, enums, errors      database/   engine + session
  tests/
frontend/
  index.html  styles.css  app.js  vendor/cytoscape.min.js
```
