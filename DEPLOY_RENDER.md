# Deploy to Render

## 1) Push this project to GitHub
- Create a new GitHub repo.
- Upload this project files.

## 2) Create a new Web Service in Render
- In Render dashboard, click **New +** -> **Blueprint**.
- Select your GitHub repo.
- Render will detect `render.yaml` and create the web service.

## 3) Environment and DB
- `SECRET_KEY` is auto-generated.
- `DATABASE_URL` is set to `sqlite:////tmp/olympiads.db`.
- On Render free tier, this SQLite file is **ephemeral** (can reset on restart/redeploy).
- The app auto-creates tables and auto-seeds starter competitions if DB is empty.

## 4) Deploy
- Click **Apply** / **Create Services**.
- Wait until build is complete.
- Open the provided Render URL.

## Notes
- Start command is `gunicorn run:app`.
- If you rename the entrypoint file, update `startCommand` in `render.yaml`.
- If you need persistent data, use:
  - Render paid plan with persistent disk, or
  - External DB (e.g. PostgreSQL).
